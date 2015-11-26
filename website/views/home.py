from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from app.project.models import Project

def home(request):
	project = Project.objects.last()
	context = {
		'project': project
	}
	return render(request, 'website/home.html', context)