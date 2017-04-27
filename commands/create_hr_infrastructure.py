# Copyright (c) AppDynamics, Inc., and its affiliates
# 2015
# All Rights Reserved
from util import CommandInvocationError, CommandExecutionError
from commands.rule_functions import get_tiers, create_infrastructure_rules, create_rules_file, post_rules_file

USAGE = "create_hr_infrastructure [args...]"

ABOUT = """Create set of standard health rules for monitoring application infrastructure.
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

def command(options, args):
    if not options:
        raise CommandInvocationError('missing command: create_hr_infrastructure [args...]')
    tiers=get_tiers(**options)
    rules=create_infrastructure_rules('OPS', '#', tiers, **options)
    filename=create_rules_file('rules_output/infra_rules.xml',rules)
    response=post_rules_file(filename, **options)
    print response
