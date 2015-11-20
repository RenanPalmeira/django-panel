# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_auth

@login_required
def logout(request):
    logout_auth(request)
    return redirect('/login/')