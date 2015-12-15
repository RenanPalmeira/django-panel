from __future__ import unicode_literals

import logging

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

logger = logging.getLogger('panel')

from board.app.news.tasks import crowler_site

#@login_required
def home(request):
	crowler_site.delay('e')
	context = {}
	return render(request, 'news/news.html', context)