from __future__ import unicode_literals

import getpass
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.translation import activate
from django.utils.translation import ugettext_lazy as _

from app.account.models import Account

user_language = settings.LANGUAGE_CODE[:2]

activate(user_language)

class Command(BaseCommand):
	def handle(self, **options):

		call_command('migrate', verbosity=0, interactive=False)
		call_command('loaddata', 'application', verbosity=0, interactive=False)

		name = raw_input(_('Name of project: '))
		site = raw_input(_('Site of project: '))
		
		email = raw_input(_('E-Mail: '))
		username = raw_input(_('Username: '))
		password = getpass.getpass()
		
		try:
			
			account = Account()
			account.username = username
			account.email = email
			account.set_password(password)
			account.save()
		except Exception, e:
			raise "Open issues in https://github.com/RenanPalmeira/django-panel/issues"