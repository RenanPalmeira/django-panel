from __future__ import unicode_literals

from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ['email', 'password']
		widgets = {
            'password': forms.PasswordInput(),
        }