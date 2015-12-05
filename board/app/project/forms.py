from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from board.core.account.models import Account
from .models import Project


class ProjectForm(forms.ModelForm):
	account = forms.ModelChoiceField(queryset=Account.objects.all())
	class Meta:
		model = Project
		fields = ['name', 'account']