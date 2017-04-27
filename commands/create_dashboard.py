# Copyright (c) AppDynamics, Inc., and its affiliates
# 2015
# All Rights Reserved
from util import CommandInvocationError, CommandExecutionError
from commands.rule_functions import get_healthrules, get_tiers_with_details, get_application_name
from commands.rule_functions import get_infrastructure_hrs, get_transaction_hrs
from commands.rule_functions import get_bt_details
from commands.widget_functions import *

USAGE = "create_dashboard [args...]"

ABOUT = """Create a standard dashboard for each tier in the application.
"""

OPTIONS = {
     'controllerHost': {
          'short': 'c',
          'help': 'Controller host name (and port)',
          'value': True,
          'value_help': '',
          'required': True
     },
     'username': {
          'short': 'u',
          'help': 'User name to run the command with.',
          'value': True,
          'value_help': '',
          'required': True
     },
     'password': {
          'short': 'p',
          'help': 'Password to run the command with.',
          'value': True,
          'value_help': '',
          'required': True
     },
     'application': {
          'short': 'a',
          'help': 'Application ID in AppDynamics.',
          'value': True,
          'value_help': '',
          'required': True
     },
     'tierFilter': {
          'short': 't',
          'help': 'Tier ID(s) for specified Application in AppDynamics or * for all tiers in Application.',
          'value': True,
          'value_help': '',
          'required': True
     },
}

DRILLDOWN_URLS = {
    'bt': '%s/controller/#/location=APP_BT_DETAIL&timeRange=last_15_minutes.BEFORE_NOW.-1.-1.15&application=%s&dashboardMode=force',
    'eventStream': '%s/controller/#/location=APP_COMPONENT_EVENTSTREAM_LIST&timeRange=last_15_minutes.BEFORE_NOW.-1.-1.15&application=%s&component=%s'
}

def command(options, args):
    if not options:
        raise CommandInvocationError('missing command: create_dashboard [args...]')
    application_name = get_application_name(**options)
    rules=get_healthrules(**options)
    tiers=get_tiers_with_details(**options)
    bts=get_bt_details('*', **options)
    status_dashboards={}
    for tier in tiers:
        infra_hrs = get_infrastructure_hrs('#', rules, tiers[tier]['tierName'])
        transaction_hrs = get_transaction_hrs('#', rules, tiers[tier]['tierName'])
        x = 25
        y = 10
        status_widget_height = 140
        status_widget_width = 140
        status_dashboard = create_status_dashboard(tiers[tier]['tierName'])
        infra_row = create_row_in_status_dashboard(
                        status_widget_height,
                        status_widget_width,
                        x, y,
                        application_name,
                        'Application Infrastructure',
                        infra_hrs
                    )
        y = y + 50 + status_widget_height + 50
        transaction_drilldown_url = DRILLDOWN_URLS['bt'] \
                    % (options['controllerHost'], options['application'])
        transaction_row = create_row_in_status_dashboard(
                            status_widget_height,
                            status_widget_width,
                            x, y,
                            application_name,
                            'Key Transactions',
                            transaction_hrs,
                            bts,
                            transaction_drilldown_url
                           )
        eventstream_drilldown_url = DRILLDOWN_URLS['eventStream'] \
                    % (options['controllerHost'], options['application'], tier)
        event_stream_widget = create_eventstream_widget(application_name, tiers[tier]['tierName'])
        event_stream_link_widget = create_eventstream_link_widget(eventstream_drilldown_url)
        status_dashboard["widgetTemplates"].extend(infra_row)
        status_dashboard["widgetTemplates"].extend(transaction_row)
        status_dashboard["widgetTemplates"].append(event_stream_widget)
        status_dashboard["widgetTemplates"].append(event_stream_link_widget)
        status_dashboards[tiers[tier]['tierName']] = status_dashboard
    for key in status_dashboards:
        file_name = 'dashboard_output/status_dashboard_%s.json' % (key)
        create_dashboard_file(file_name, status_dashboards[key])
