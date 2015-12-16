from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	context = {}
	return render(request, 'news/news.html', context)