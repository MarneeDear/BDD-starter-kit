import os
from behaving import environment as benv

PERSONAS = {}

def before_all(context):
    # import mypackage
    # context.attachment_dir = os.path.join(os.path.dirname(mypackage.__file__), 'tests/data')
    # context.sms_path = os.path.join(os.path.dirname(mypackage.__file__), '../../var/sms/')
    # context.gcm_path = os.path.join(os.path.dirname(mypackage.__file__), '../../var/gcm/')
    # context.mail_path = os.path.join(os.path.dirname(mypackage.__file__), '../../var/mail/')
    benv.before_all(context)


def after_all(context):
    benv.after_all(context)


def before_feature(context, feature):
    benv.before_feature(context, feature)


def after_feature(context, feature):
    benv.after_feature(context, feature)


def before_scenario(context, scenario):
    benv.before_scenario(context, scenario)
    context.personas = PERSONAS

def after_scenario(context, scenario):
    benv.after_scenario(context, scenario)