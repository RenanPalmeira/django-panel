from __future__ import unicode_literals

from django.db import models

from board.core.account.models import Account
from board.core.application.models import Application

class Project(models.Model):
	id_project = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	site = models.EmailField(max_length=155, null = True)

	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	class Meta:
		app_label = "project"
		db_table = "project"

class ProjectAccount(models.Model):
	id_project_account = models.AutoField(primary_key=True)

	project = models.ForeignKey(Project)
	account = models.ForeignKey(Account)

	level = models.SmallIntegerField(default=1)

	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	class Meta:
		app_label = "project"
		db_table = "project_account_set"

class ProjectApplication(models.Model):
	id_project_application = models.AutoField(primary_key=True)

	project = models.ForeignKey(Project)
	application = models.ForeignKey(Application)

	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	class Meta:
		app_label = "project"
		db_table = "project_application_set"