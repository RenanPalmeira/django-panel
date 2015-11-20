# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth

def login(request):
	print request.user.is_authenticated()
	return render(request, "login.html", {})
