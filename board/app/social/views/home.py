from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from board.app.social.models import ProviderSocial
from board.core.provider.twitter import TwitterProvider

@login_required
def home(request):
	provider = ProviderSocial.objects.all()
	context = {
		'provider': provider
	}
	return render(request, 'social/social.html', context)

@login_required
def twitter(request):
	try:
		redirect_url = TwitterProvider.get_authorization_url()
	except Exception, e:
		redirect_url = ''
	
	context = {
		'redirect_url': redirect_url,
	}
	return render(request, 'social/social.html', context)