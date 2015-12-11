from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from board.app.social.models import ProviderSocial

@login_required
def home(request):
	provider = ProviderSocial.objects.all()
	context = {
		"provider": provider
	}
	return render(request, 'social/social.html', context)