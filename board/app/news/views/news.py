from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from board.app.news.models import ArticleConfiguration
from board.app.news.forms import ArticleForm

@login_required
def home(request):
	form = ArticleForm()
	configuration = ArticleConfiguration.objects.all()
	context = {
		'form': form,
		'configuration': configuration,
	}
	return render(request, 'news/news.html', context)