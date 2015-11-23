from __future__ import unicode_literals

from rest_framework import serializers
from app.core.models import Application

class ApplicationSerializer(serializers.ModelSerializer):
	class Meta:
 		model = Application
		fields = ('name', 'color',)