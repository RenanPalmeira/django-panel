from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

class Account(AbstractBaseUser):
	id_account = models.AutoField(primary_key=True)
	username = models.CharField(max_length=255, unique = True)
	email = models.EmailField(max_length=255)
	
	first_name = models.CharField(max_length=255, null = True)
	last_name = models.CharField(max_length=255, null = True)

	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	USERNAME_FIELD = ('username')
	REQUIRED_FIELDS = []

	def __unicode__(self):
		return self.username
	
	@property
	def is_staff(self):
		return bool(self.status)
		
	class Meta:
		app_label = "account"
		db_table = "account"