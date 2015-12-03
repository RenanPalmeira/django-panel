from __future__ import unicode_literals

from rest_framework import serializers
from .models import ProviderSocial

class SocialSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProviderSocial
		fields = ('name', )