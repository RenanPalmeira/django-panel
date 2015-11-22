from __future__ import unicode_literals

from django.db import models

class Client(models.Model):
	id_client = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250)
	slug = models.SlugField(null = True)
	icon = models.CharField(max_length=155, null = True)
	keywords = models.CharField(max_length=155, null = True)
	author = models.CharField(max_length=155, null = True)
	description = models.CharField(max_length=155, null = True)
	color = models.CharField(max_length=155, null = True)
	image = models.CharField(max_length=155, null = True)
	
	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	def __unicode__(self):
		return self.client

	class Meta:
		db_table = "client"

class Login(models.Model):
	id_login = models.AutoField(primary_key=True)
	client = models.ForeignKey('Client')
	email = models.CharField(max_length=250)
	password = models.CharField(max_length=250)

	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	class Meta:
		db_table = "login"