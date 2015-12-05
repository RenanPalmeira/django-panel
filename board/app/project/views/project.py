from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from board.app.project.models import Project
from board.app.project.forms import ProjectForm

@login_required
def home(request):
	project = Project.objects.last()
	form  = ProjectForm(instance=project)
	context = {
		'name': 'Projeto',
		'form': form
	}
	return render(request, 'project/project.html', context)