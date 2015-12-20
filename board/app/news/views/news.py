from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.utils.translation import ugettext as _

from board.app.news.models import ArticleConfiguration
from board.app.project.models import Project
from board.app.news.forms import ArticleForm

@login_required
def home(request):
	form = ArticleForm()
	configuration = ArticleConfiguration.objects.all()

	if request.method == 'POST':
		project = Project.objects.last()
		form = ArticleForm(request.POST)
		if form.is_valid():
			try:
				article = form.save(commit=False)
				article.account = request.user
				article.project = project
				article.save()
				messages.success(request, _('News saved'))
			except Exception, e:
				messages.error(request, _('Erro interno 500 - ')+str(e))
		else:
			messages.error(request, _('incorrect fields'))

	context = {
		'form': form,
		'configuration': configuration,
	}
	return render(request, 'news/news.html', context)