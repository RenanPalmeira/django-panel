from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def form(request):
	return render(request, 'configuration/form.html', {})