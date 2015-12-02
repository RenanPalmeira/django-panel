# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_auth

@never_cache
@login_required
def logout(request):
    logout_auth(request)
    return redirect('/login/')