#!/usr/bin/env python

from __future__ import unicode_literals, with_statement

from fabric.api import local, settings, task, run
from fabric.contrib.console import confirm

def test():
	"""
	fab test
	"""
	with settings(warn_only=True):
		result = local('./manage.py test', capture=True)
	
	if result.failed and not confirm("Tests failed. Continue anyway?"):
		abort("Aborting at user request.")

@task
def start(path = None, port = 8000):
	if not path is None:
		run("python %s/manage.py runserver 127.0.0.1:%s" % (path,port))
	else:
		run("./manage.py runserver 127.0.0.1:%s" % (port))