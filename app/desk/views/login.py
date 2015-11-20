# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth

from app.account.forms import AccountForm

def login(request):
	if request.user.is_authenticated():
		return redirect('/desk')
		
	form = AccountForm()
	if request.method == 'POST':
		form = AccountForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			user = authenticate(email=email, password=password)
			if not user is None:
				login_auth(request, user)
			return redirect('/desk')
	context = {
		"form": form
	}
	return render(request, "login.html", context)
