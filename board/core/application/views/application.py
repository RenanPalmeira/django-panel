from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils.module_loading import import_string
from django.contrib.auth.decorators import login_required

from board.core.application.models import Application

from django.template import loader, TemplateDoesNotExist

@login_required
def home(request, slug = None):
	context = {}
	if not slug is None:
		app = get_object_or_404(Application, slug=slug)
		try:
			view = import_string('board.app.%s.views.home' % slug)
			return view(request)
		except Exception, e:
			print e
		
	return render(request, "application/application.html", context)