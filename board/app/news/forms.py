from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from board.core import widgets
from .models import ArticleConfiguration, Article

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'reference', 'content',]
		widgets = {
            'content': forms.Textarea(attrs = {'rows': 10}),
        }