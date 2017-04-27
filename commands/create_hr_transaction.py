# Copyright (c) AppDynamics, Inc., and its affiliates
# 2015
# All Rights Reserved
from util import CommandInvocationError, CommandExecutionError
from commands.rule_functions import get_bt_details, create_bt_rules, create_rules_file, post_rules_file

USAGE = "create_hr_transaction [args...]"

ABOUT = """Create set of standard health rules for monitoring key transactions.
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
     'transactionFilter': {
          'short': 't',
          'help': 'IDs of business transactions for which to create health rules (comma-separated)',
          'value': True,
          'value_help': '',
          'required': True
     },
}

def command(options, args):
    if not options:
        raise CommandInvocationError('missing command: create_hr_transaction [args...]')
    bts=get_bt_details(**options)
    rules=create_bt_rules('OPS', '#', bts, **options)
    filename=create_rules_file('rules_output/transaction_rules.xml',rules)
    response=post_rules_file(filename, **options)
    print response
