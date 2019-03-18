import logging
import os
import sys
import threading
from .middlewares import get_current_db_name

# from rest_models.router import get_default_api_database
from rest_models.router import RestModelRouter

logger = logging.getLogger(__name__)


class TenantRouter(RestModelRouter):
    def get_api_database(self, model):
        if self.is_api_model(model):
            result = get_current_db_name()
            # logger.debug("DB name for %s:%s", model, result)
        else:
            result = None
        return result
    
    def db_for_read(self, model, **hints):
        return self.get_api_database(model)

    def db_for_write(self, model, **hints):
        return self.get_api_database(model)
    
