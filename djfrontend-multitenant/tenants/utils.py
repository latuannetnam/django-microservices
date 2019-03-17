import logging
import os
import sys

LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler(sys.stdout)
# ch.setLevel(LOG_LEVEL)
ch.setFormatter(formatter)
logger.addHandler(ch)
# # create file handler which logs even debug messages
# WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
# # fh = logging.FileHandler(WORKING_DIR + '/monitor-admin.log', mode='a')
# fh = logging.FileHandler('/tmp/monitor-admin.log', mode='a')
# # fh.setLevel(logging.DEBUG)
# fh.setFormatter(formatter)
# logger.addHandler(fh)


def hostname_from_request(request):
    return request.get_host().split(":")[0].lower()


def tenant_db_from_request(request):
    hostname = hostname_from_request(request)
    logger.debug("request hostname: %s", hostname)
    tenants_map = get_tenants_map()
    logger.debug("tennant: %s", tenants_map.get(hostname))
    return tenants_map.get(hostname)


def get_tenants_map():
    return {"site1.test.com": "site1", "site2.test.com": "site2"}
