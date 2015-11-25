from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Account

class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ['email', 'password']
		widgets = {
            'password': forms.PasswordInput(attrs = {'placeholder':_('Password')}),
        }