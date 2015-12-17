from __future__ import unicode_literals

from django.core.management import call_command, base

class Command(base.BaseCommand):
	def handle(self, **options):
		call_command('migrate', verbosity=0, interactive=False)
		call_command('loaddata', 'application', 'providersocial', 'articleconfiguration', verbosity=0, interactive=False)
		call_command('compilemessages', verbosity=0, interactive=False)