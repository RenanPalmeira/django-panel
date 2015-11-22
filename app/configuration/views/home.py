# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.core.models import Application

@login_required
def home(request):
	context = {}
	return render(request, "configuration/index.html", context)