from datetime import timedelta
import os
from typing import Dict, Union

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

fault_log_file_path = os.getenv('FAULT_LOG_FILE_PATH', 'fault.log')
google_analytics_api_key = os.getenv('GOOGLE_ANALYTICS_API_KEY', '')
logging_config_file_path = os.getenv('LOGGING_CONFIG_FILE_PATH', '..\logging_config.json')
login_api = os.getenv('LOGIN_API', '')
register_title_api = os.getenv('REGISTER_TITLE_API', '')
secret_key = os.getenv('APPLICATION_SECRET_KEY' ,'secretkeyshouldberandom')
service_notice_html = os.getenv('SERVICE_NOTICE_HTML', '<h2>Downtime notice</h2><p>This service will be offline between 2.00&ndash;5.00 on 31st July</p>')
session_cookie_secure = os.getenv('SESSION_COOKIE_SECURE', 'False').lower() != 'false'
more_proprietor_details = os.getenv('MORE_PROPRIETOR_DETAILS', 'False')
show_full_title_data = os.getenv('SHOW_FULL_TITLE_DATA', 'True').lower() == 'true'
show_full_title_pdf = os.getenv('SHOW_FULL_TITLE_PDF', 'True').lower() == 'true'


CONFIG_DICT = {
    'DEBUG': False,
    'FAULT_LOG_FILE_PATH': fault_log_file_path,
    'GOOGLE_ANALYTICS_API_KEY': google_analytics_api_key,
    'LOGGING': True,
    'LOGGING_CONFIG_FILE_PATH': logging_config_file_path,
    'LOGIN_API': login_api,
    'PERMANENT_SESSION_LIFETIME': timedelta(minutes=15),
    'REGISTER_TITLE_API': register_title_api,
    'SECRET_KEY': secret_key,
    'SERVICE_NOTICE_HTML': service_notice_html,
    'SESSION_COOKIE_SECURE': session_cookie_secure,
    'MORE_PROPRIETOR_DETAILS': more_proprietor_details,
    'SHOW_FULL_TITLE_DATA': show_full_title_data,
    'SHOW_FULL_TITLE_PDF': show_full_title_pdf,
}  # type: Dict[str, Union[bool, str, timedelta]]

# <worldpay> (From https://gh-svn-d01.diti.lr.net/svn/eservices/branches/release1415/ECBX_PortServicesBackEnd).
CONFIG_DICT.update({'DEBUG': True})
WP_TEST_MODE_ON = 100
WP_TEST_MODE_OFF = 0

WORLDPAY_DICT = {
    'BYPASS_WORLDPAY': 'N',
    'PURCHASE_TIME_EXPIRY_LIMIT': '5',
    ##'WORLDPAY_REDIRECT_URL': 'https://secure.worldpay.com/wcc/dispatcher',
    'WORLDPAY_REDIRECT_URL': os.getenv('WORLDPAY_REDIRECT_URL', 'https://secure-test.worldpay.com/wcc/purchase'),
    'WP_AUTH_CURR': 'GBP',
    'WP_CALLBACK_PW': 'unknown',
    'KEYSTORE_FILE_PATH': '/web/sycell/config/lronline.pfx',
    'KEYSTORE_SECRET': 'trust',
    'WP_INST_ID': os.getenv('WP_INST_ID', ''),
    'WP_AUTH_MODE': 'E',
    'WP_ACCOUNT_ID': os.getenv('WP_ACCOUNT_ID', ''),
    'WP_TEST_MODE': WP_TEST_MODE_ON,
    'WP_DEFAULT_COUNTRY': 'GB',
    'WP_HOSTNAME_FOR_POST_AUTH': 'select.worldpay.com',
    'WP_PORT_FOR_POST_AUTH': '443',
    'WP_URLEND_FOR_POST_AUTH': '/wcc/authorise',
    'WP_PASSWORD_FOR_POST_AUTH': os.getenv('WP_PASSWORD_FOR_POST_AUTH',''),
    'WP_OP_FOR_POST_AUTH': 'postAuth-full',
    'WP_TESTMODE_FOR_POST_AUTH': WP_TEST_MODE_ON,
    'WP_INST_ID_FOR_POST_AUTH': os.getenv('WP_INST_ID_FOR_POST_AUTH', ''),
    'WORLDPAY_START_ADDRESS': '195.35.90.0',
    'WORLDPAY_FINISH_ADDRESS': '195.35.91.255',
    'WP_AUTHORISATION_CALLBACK_URL': 'testpayment.landregisteronline.gov.uk/lro/servlet/AuthorisationCallbackServlet',
    'WP_CALLBACK_SERVER_URL': os.getenv('WP_CALLBACK_SERVER_URL', 'http://localhost:5000/callback'),
    'RT_CONTEXT ': ' "https://localhost:10035"',
    'AVS_CHECK_ON': 'N',
    'AVS_FAILED_MATCH': '4',
    'BACKDOOR': 'false',
    'CONFIRM_PAYMENT_URL': '/wps/myportal/QDMPS-ProtectedServlets/ConfirmPayment?',
    'ACTION_URL1': '/download.do',
    'ACTION_URL2': '/QuickEnquiryInit.do',
    'ACTION_URL3': ''
}
#</worldpay>

# N.B: we do not want 'live' by default - it should be set explicitly in the environment, as required.
settings = os.getenv('SETTINGS', 'DEV').lower()

if settings == 'live':
    WORLDPAY_DICT['WP_TEST_MODE'] = WP_TEST_MODE_OFF
    CONFIG_DICT['DEBUG'] = False
elif settings == 'dev':
    CONFIG_DICT['DEBUG'] = True
elif settings == 'test':
    # We do NOT set TESTING to True here as it turns off authentication, and we
    # want to make sure the app behaves the same when running tests locally
    # as it does in production.
    CONFIG_DICT['DEBUG'] = True
    CONFIG_DICT['DISABLE_CSRF_PREVENTION'] = True
    CONFIG_DICT['FAULT_LOG_FILE_PATH'] = '/dev/null'
    CONFIG_DICT['LOGGING'] = False
    CONFIG_DICT['SLEEP_BETWEEN_LOGINS'] = False
