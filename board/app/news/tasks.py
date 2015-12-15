from __future__ import unicode_literals, absolute_import

import logging
from celery import shared_task

logger = logging.getLogger(__name__)

from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def crowler_site(tweet):
    try:
        logger.info('Test in celery')
        logger.error('Test in celery')
        logger.warning('Test in celery')
    except Exception, e:
        print e
        logger.error(e)