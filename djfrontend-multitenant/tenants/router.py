import logging
import os
import sys
from .middlewares import get_current_db_name

# from rest_models.router import get_default_api_database
from rest_models.router import RestModelRouter

LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler(sys.stdout)
# ch.setLevel(LOG_LEVEL)
ch.setFormatter(formatter)
logger.addHandler(ch)


class TenantRouter(RestModelRouter):
    @staticmethod
    def is_api_model(model):
        return hasattr(model, 'APIMeta')

    def get_api_database(self, model):
        if self.is_api_model(model):
            # if hasattr(model.APIMeta, 'db_name'):
            #     result = model.APIMeta.db_name
            # else:
            #     result = get_current_db_name()
            result = get_current_db_name()
        else:
            result = None
        logger.debug("DB name for %s:%s", model, result)
        return result
    
    def db_for_read(self, model, **hints):
        return self.get_api_database(model)

    def db_for_write(self, model, **hints):
        return self.get_api_database(model)
    
