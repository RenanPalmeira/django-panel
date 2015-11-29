from __future__ import unicode_literals
from django.db import models

class Application(models.Model):
	id_application = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250)
	slug = models.SlugField()
	icon = models.CharField(max_length=155)
	color = models.CharField(max_length=155)
	order = models.SmallIntegerField(null=True, blank=False)

	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return 'app/'+self.slug

	class Meta:
		db_table = "application"