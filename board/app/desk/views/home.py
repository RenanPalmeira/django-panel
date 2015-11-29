# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from board.core.application.models import Application
@login_required
def home(request):
	apps = Application.objects.all()
	context = {
		"apps": apps
	}
	return render(request, "desk/index.html", context)