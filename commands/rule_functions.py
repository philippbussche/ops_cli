import requests
import json
import xmltodict
import collections
from commands.templates import hr_infrastructure as hr_infra
from commands.templates import hr_transaction as hr_trans
from util import CommandInvocationError, CommandExecutionError


# Helper function to request data in json
def get_data(endpoint, username, password, json=True):
    if json is True:
        param = {'output': 'json'}
    else:
        param = {}
    response = requests.get(endpoint,
                            auth=(username, password),
                            params=param)
    if json is True:
        return response.json()
    else:
        return response.text


# Return the name of the application given its ID
def get_application_name(**kwargs):
    application_id = kwargs['application']
    endpoint = 'http://%s/controller/rest/applications' \
        % (kwargs['controllerHost'])
    try:
        data = get_data(endpoint, kwargs['username'], kwargs['password'])
    except:
        raise CommandInvocationError('Error fetching application name.')
    for application in data:
        if str(application['id']) == str(application_id):
            return application['name']


# Return list of tier names for given application and filter
def get_tiers(**kwargs):
    tier_names = []
    tier_filter = kwargs['tierFilter']
    endpoint = 'http://%s/controller/rest/applications/%s/tiers' \
        % (kwargs['controllerHost'], kwargs['application'])
    try:
        data = get_data(endpoint, kwargs['username'], kwargs['password'])
    except:
        raise CommandInvocationError('Error fetching tiers from application.')
    for tier in data:
        if tier_filter == '*':
            tier_names.append(tier['name'])
        elif tier['name'] in tier_filter:
            tier_names.append(tier['name'])
    return tier_names


# Return dictionary of tiers with some details
def get_tiers_with_details(**kwargs):
    tiers = {}
    tier_filter = kwargs['tierFilter']
    endpoint = 'http://%s/controller/rest/applications/%s/tiers' \
        % (kwargs['controllerHost'], kwargs['application'])
    try:
        data = get_data(endpoint, kwargs['username'], kwargs['password'])
    except:
        raise CommandInvocationError('Error fetching tiers from application.')
    for tier in data:
        if tier['name'] in tier_filter or tier_filter == '*':
            t = {'tierName': tier['name']}
            tiers[tier['id']] = t
    return tiers


# Check whether the given tier has JDBC metrics
def has_jdbc_metrics(tier_id, **kwargs):
    endpoint = "http://%s/controller/rest/applications/%s/metric-data?metric-path=Application Infrastructure Performance|%s|JMX|JDBC Connection Pools|%s|Active Connections&time-range-type=BEFORE_NOW&duration-in-mins=15" \
        % (kwargs['controllerHost'], kwargs['application'], tier_id, '*')
    try:
        data = get_data(endpoint, kwargs['username'], kwargs['password'])
    except:
        raise CommandInvocationError('Error verifying if tier has JDBC metrics.')
    if len(data) > 0:
        return True
    else:
        return False


def get_infra_rule_name_pattern(prefix, delimiter, application_name):
    rule_name_pattern = '%s%s%s%s%s%s%s_%s' \
                % (prefix, delimiter,
                    application_name, delimiter,
                    '%%TIER%%', delimiter,
                    'INFRASTRUCTURE',
                    '%%SCOPE%%')
    return rule_name_pattern


# Create infrastructure rules XML string
def create_infrastructure_rules(prefix, delimiter, tiers, **options):
    rules = []
    application_name = get_application_name(**options)
    rule_name = get_infra_rule_name_pattern(prefix, delimiter, application_name)
    for tier in tiers:
        heap = hr_infra.xmlTemplateServiceHealthRule_HEAP \
            .replace('%%RULENAME%%', rule_name) \
            .replace('%%TIER%%', tier) \
            .replace('%%SCOPE%%', 'HEAP')
        rules.append(heap)
        gc = hr_infra.xmlTemplateServiceHealthRule_GC \
            .replace('%%RULENAME%%', rule_name) \
            .replace('%%TIER%%', tier) \
            .replace('%%SCOPE%%', 'GC')
        rules.append(gc)
        threads = hr_infra.xmlTemplateServiceHealthRule_THREADS \
            .replace('%%RULENAME%%', rule_name) \
            .replace('%%TIER%%', tier) \
            .replace('%%SCOPE%%', 'THREADS')
        rules.append(threads)
        if has_jdbc_metrics(tier, **options):
            jdbc = hr_infra.xmlTemplateServiceHealthRule_JDBC \
                .replace('%%RULENAME%%', rule_name) \
                .replace('%%TIER%%', tier) \
                .replace('%%SCOPE%%', 'JDBC')
            rules.append(jdbc)
    return ''.join(rules)


# Create rules file
def create_rules_file(filename, rules):
    xml = open(filename, 'w')
    xml.truncate()
    xml.write('<health-rules controller-version=\"004-002-005-001\">')
    xml.write(rules)
    xml.write('</health-rules>')
    xml.close()
    return filename


# Post rules file to Controller in order to import Health Rules
def post_rules_file(file, **kwargs):
    params = {"overwrite": "true"}
    files = {'file': ('fileUpload', open(file, 'rb'),
                      'application/xml', {'Expires': '0'})}
    endpoint = 'http://%s/controller/healthrules/%s' \
        % (kwargs['controllerHost'], kwargs['application'])
    try:
        r = requests.post(endpoint,
                          params=params,
                          auth=(kwargs['username'], kwargs['password']),
                          files=files)
        # print r._content
        return r._content
    except:
        raise CommandInvocationError('Error posting rules XML.')


# Cut name after 15 characters
def get_bt_display_name(bt_name):
    return bt_name[:15]


# Return dictionary containing business transaction details
def get_bt_details(transaction_filter=None, **kwargs):
    result = {}
    if transaction_filter is None:
        transaction_filter = kwargs['transactionFilter']
    endpoint = 'http://%s/controller/rest/applications/%s/business-transactions' \
        % (kwargs['controllerHost'], kwargs['application'])
    try:
        data = get_data(endpoint, kwargs['username'], kwargs['password'])
        # print data
    except:
        raise CommandInvocationError('Error fetching business transaction details.')
    for transaction in data:
        transaction_id = str(transaction['id'])
        if transaction_id in transaction_filter or transaction_filter == '*':
            t = {
                'tierName': transaction['tierName'],
                'btName': transaction['name'],
                'displayName': get_bt_display_name(transaction['name'])
            }
            result[transaction_id] = t
    if len(result) == 0:
        raise CommandInvocationError('No business transactions found for the specified IDs.')
    return result


def get_bt_rule_name_pattern(prefix, delimiter, application_name):
    rule_name_pattern = '%s%s%s%s%s%s%s_%s' \
                % (prefix, delimiter,
                    application_name, delimiter,
                    '%%TIER%%', delimiter,
                    'USERBT',
                    '%%DISPLAYNAME%%')
    return rule_name_pattern


# Create business transaction rules XML string
def create_bt_rules(prefix, delimiter, bts, **kwargs):
    rules = []
    application_name = get_application_name(**kwargs)
    rule_name = get_bt_rule_name_pattern(prefix, delimiter, application_name)
    for key in bts:
        rule = hr_trans.xmlTemplateTransactionHealthRule_BT \
            .replace('%%RULENAME%%', rule_name) \
            .replace('%%TIER%%', bts[key]['tierName']) \
            .replace('%%DISPLAYNAME%%', bts[key]['displayName']) \
            .replace('%%BTNAME%%', bts[key]['btName'])
        rules.append(rule)
    return ''.join(rules)

# Get all healthrules for the application
def get_healthrules(**kwargs):
    endpoint = 'http://%s/controller/healthrules/%s' \
        % (kwargs['controllerHost'], kwargs['application'])
    try:
        data = get_data(endpoint, kwargs['username'], kwargs['password'], json=False)
    except:
        raise CommandInvocationError('Error fetching health rules.')
    return data


# Return true if XML data contains application infrastructure rules
def get_infrastructure_hrs(delimiter, rules, tier):
    custom_rules = {}
    doc = xmltodict.parse(rules)
    for hr in doc['health-rules']['health-rule']:
        try:
            name_split = hr['name'].split(delimiter)
            if 'INFRASTRUCTURE' in name_split[3] and tier in name_split[2]:
                scope_split = name_split[3].split('_')
                r = {'displayName': scope_split[1]}
                custom_rules[hr['name']] = r
        except:
            # this rule apparently does not follow the expected pattern
            # might be an OOTB rule
            pass
    return collections.OrderedDict(sorted(custom_rules.items()))

# Return true if XML data contains application infrastructure rules
def get_transaction_hrs(delimiter, rules, tier):
    custom_rules = {}
    doc = xmltodict.parse(rules)
    for hr in doc['health-rules']['health-rule']:
        try:
            name_split = hr['name'].split(delimiter)
            if 'USERBT' in name_split[3] and tier in name_split[2]:
                scope_split = name_split[3].split('_')
                btName = hr['affected-entities-match-criteria']['affected-bt-match-criteria']['business-transactions']['business-transaction']['#text']
                r = {
                        'displayName': scope_split[1],
                        'btName': btName
                    }
                custom_rules[hr['name']] = r
        except:
            # this rule apparently does not follow the expected pattern
            # might be an OOTB rule
            pass
    return collections.OrderedDict(sorted(custom_rules.items()))
