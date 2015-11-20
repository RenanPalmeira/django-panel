# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth

from app.account.forms import AccountForm

def login(request):
	form = AccountForm()
	context = {
		"form": form
	}
	return render(request, "login.html", context)
