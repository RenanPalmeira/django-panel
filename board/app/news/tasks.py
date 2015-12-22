from __future__ import unicode_literals, absolute_import

import logging
from celery.task import task

logger = logging.getLogger(__name__)

@task
def send_link(x, y):
    return x + y