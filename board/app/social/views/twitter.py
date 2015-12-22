from __future__ import unicode_literals

import logging

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from board.app.social.models import Social
from board.core.provider.twitter import TwitterProvider

logger = logging.getLogger(__name__)

@login_required
def twitter(request):
	try:
		redirect_url = TwitterProvider.get_authorization_url()
		request.session['request_token'] = TwitterProvider.request_token
	except Exception, e:
		logger.debug(e)
		redirect_url = ''
	
	context = {
		'redirect_url': redirect_url,
	}
	return render(request, 'social/twitter.html', context)

@login_required
def twitter_callback(request):
	account = request.user
	
	oauth_token = request.GET.get('oauth_token', None)
	oauth_verifier = request.GET.get('oauth_verifier', None)
	request_token = request.session.get('request_token', None)
	
	if not oauth_token is None and not oauth_verifier is None and not request_token is None:
		try:
			TwitterProvider.request_token = request_token
			TwitterProvider.get_access_token(oauth_verifier)

			access_token = TwitterProvider.access_token
			access_token_secret	= TwitterProvider.access_token_secret	

			social = Social(account = account, token = access_token, secret = access_token_secret)
			social.save()

		except Exception, e:
			logger.error(e)

	return redirect('/desk#social/twitter')