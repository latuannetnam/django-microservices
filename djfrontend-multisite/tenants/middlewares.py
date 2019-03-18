# https://github.com/agiliq/building-multi-tenant-applications-with-django/blob/master/isolated-db/tenants/middlewares.py
import threading
from uuid import uuid4
import logging
import os
import sys
import time
from django.db import connections
from .utils import tenant_db_from_request

logger = logging.getLogger(__name__)

THREAD_LOCAL = threading.local()


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        db = tenant_db_from_request(request)
        logger.debug("Set DB from request:%s", db)
        set_db_for_router(db)
        # time.sleep(5)
        response = self.get_response(request)
        return response


def get_current_db_name():
    logger.debug("Get DB from middleware:%s", getattr(THREAD_LOCAL, "DB", None))
    return getattr(THREAD_LOCAL, "DB", None)


def set_db_for_router(db):
    setattr(THREAD_LOCAL, "DB", db)
