import logging
import os
import sys


logger = logging.getLogger(__name__)
# LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
# logger.setLevel(LOG_LEVEL)
# formatter = logging.Formatter(
#     '%(asctime)s - %(levelname)s - %(message)s')
# ch = logging.StreamHandler(sys.stdout)
# ch.setFormatter(formatter)
# logger.addHandler(ch)


def hostname_from_request(request):
    return request.get_host().split(":")[0].lower()


def tenant_db_from_request(request):
    hostname = hostname_from_request(request)
    logger.debug("request hostname: %s", hostname)
    return hostname
