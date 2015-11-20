from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.hashers import make_password

class Account(models.Model):
	id_account = models.AutoField(primary_key=True)
	username = models.CharField(max_length=255, unique = True)
	password = models.CharField(max_length=255)
	
	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	USERNAME_FIELD = ('username')
	REQUIRED_FIELDS = []

	def set_password(self, password):
		self.password = make_password(password)

	def __unicode__(self):
		return self.username

	class Meta:
		db_table = "application"
