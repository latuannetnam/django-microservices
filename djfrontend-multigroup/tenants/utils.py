import logging
import os
import sys


logger = logging.getLogger(__name__)


def groupname_from_request(request):
    if request.user.is_authenticated:
        user = request.user
        logger.debug("request user: %s", user)
        if len(user.groups.all()) > 0:
            group = user.groups.all()[0].name
            logger.debug("User group: %s", group)
            return group
        else:
            return None
    else:
        return None


def tenant_db_from_request(request):
    return groupname_from_request(request)    
