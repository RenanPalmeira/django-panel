from __future__ import unicode_literals, absolute_import

import re
import logging
import requests
from celery.task import task

logger = logging.getLogger(__name__)

ep = r'^http?s\:\/\/([a-z0-9\.\-\/\%\&])$'

@task
def send_link(reference):
	try:
		result = dict({})
		link = requests.get(reference)
		result['title'] = re.findall(r'<title>([a-z0-9A-Z\.\\\!\? ]+)</title>', link.text)
		return result
	except Exception, e:
		logger.warning(e)
	return None