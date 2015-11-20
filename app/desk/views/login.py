# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth

from app.account.forms import AccountForm

def login(request):
	form = AccountForm()
	if request.method == 'POST':
		form = AccountForm(request.POST)
		if form.is_valid():
			pass
	context = {
		"form": form
	}
	return render(request, "login.html", context)
