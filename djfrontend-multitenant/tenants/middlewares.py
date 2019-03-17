# https://github.com/agiliq/building-multi-tenant-applications-with-django/blob/master/isolated-db/tenants/middlewares.py
import threading
from uuid import uuid4
import logging
import os
import sys
from django.db import connections
from .utils import tenant_db_from_request

LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler(sys.stdout)
# ch.setLevel(LOG_LEVEL)
ch.setFormatter(formatter)
logger.addHandler(ch)

THREAD_LOCAL = threading.local()


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        db = tenant_db_from_request(request)
        logger.debug("DB from request:%s", db)
        setattr(THREAD_LOCAL, "DB", db)
        response = self.get_response(request)
        return response


def get_current_db_name():
    logger.debug("current DB:%s", getattr(THREAD_LOCAL, "DB", None))
    return getattr(THREAD_LOCAL, "DB", None)


def set_db_for_router(db):
    setattr(THREAD_LOCAL, "DB", db)
