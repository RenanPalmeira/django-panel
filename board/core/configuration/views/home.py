from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

@never_cache
@login_required
def home(request):
	context = {}
	return render(request, "configuration/configuration.html", context)