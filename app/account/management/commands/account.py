from __future__ import unicode_literals

import getpass
from django.core.management import call_command, base
from django.conf import settings
from django.utils.translation import activate
from django.utils.translation import ugettext_lazy as _

from app.account.models import Account
from app.project.models import Project, ProjectAccount

class Command(base.BaseCommand):
	def handle(self, **options):

		call_command('migrate', verbosity=0, interactive=False)
		call_command('loaddata', 'application', verbosity=0, interactive=False)
		call_command('compilemessages', verbosity=0, interactive=False)

		name = str(raw_input(_('Name of project: ')))
		site = str(raw_input(_('Site of project: ')))
		
		email = str(raw_input(_('E-Mail: ')))
		username = str(raw_input(_('Username: ')))
		password = getpass.getpass()
		try:

			account = Account()
			account.username = username
			account.email = email
			account.set_password(password)
			account.save()

			project = Project()
			project.name = name
			project.site = site
			project.save()

			project_account = ProjectAccount(project=project, account=account)
			project_account.save()

		except Exception, e:
			raise e