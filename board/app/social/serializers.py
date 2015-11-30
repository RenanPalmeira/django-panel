from __future__ import unicode_literals

from rest_framework import serializers
from .models import Social

class SocialSerializer(serializers.ModelSerializer):
	class Meta:
		model = Social
		fields = ('username', 'account', 'status',)