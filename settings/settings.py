import os, importlib

admin_set = importlib.import_module('settings.custom_settings')

TOKEN = os.environ['OD_BOT_TOKEN']
ADMINS = [admin.strip() for admin in os.environ.get('OD_BOT_ADMINS', '').split(',')]

HEROKU_APP_NAME = os.environ.get('OD_BOT_HEROKU_APP_NAME', False)
WEBHOOK = os.environ.get('OD_BOT_WEBHOOK_URL', False)
WEBHOOK_PORT = int(os.environ.get('OD_BOT_WEBHOOK_PORT', '8443'))
DEBUG = os.environ.get('OD_BOT_DEBUG', False)

OD_URL = os.environ.get('OD_BOT_BUILDER_URL', '') if os.environ.get('OD_BOT_BUILDER_URL', '') != '' else 'https://builder.open-decision.org'
DEMO_QUERY = admin_set.DEMO_QUERY if admin_set.DEMO_QUERY and admin_set.DEMO_QUERY != '' else os.environ.get('OD_BOT_DEMO_QUERY')
LANG = admin_set.LANG if admin_set.LANG and admin_set.LANG != '' else os.environ.get('OD_BOT_LANG', 'en')
GREET_IMAGE = admin_set.GREET_IMAGE if admin_set.GREET_IMAGE and admin_set.GREET_IMAGE != '' else os.environ.get('OD_BOT_GREET_IMAGE')
QUERY_LIST = admin_set.QUERY_LIST if admin_set.QUERY_LIST and admin_set.QUERY_LIST != [] else os.environ.get('OD_BOT_QUERY_LIST', '').split(',')

allow_language_change = False

def reload_settings():
    importlib.reload(admin_set)
