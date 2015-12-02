from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from board.core.application.models import Application

@login_required
def home(request, slug = None):
	context = {}
	if not slug is None:
		app = get_object_or_404(Application, slug=slug)
		context['app'] = app
		
	return render(request, "application/home.html", context)