from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from board.app.news.models import Article

@login_required
def listing(request):
	articles = Article.objects.all()
	context = {
		'articles': articles,
	}
	return render(request, 'news/listing.html', context)