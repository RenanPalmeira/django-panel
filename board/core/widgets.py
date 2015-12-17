from __future__ import unicode_literals

from django.forms import Widget
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.widgets import flatatt

class SwitchButtonWidth(Widget):
    """
        Exemple:
        widgets = {
            'field': widgets.SwitchButtonWidth(checked=False)
        }
    """

    checked = str()
    def __init__(self, *args, **kwargs):
        if "checked" in kwargs:
            self.checked = kwargs.pop("checked")
        Widget.__init__(self, *args, **kwargs)

    def render(self, name, value, attrs=None):
        html = '<div class=\"switch-container\">'
        if not self.checked is None and self.checked != '' and self.checked != False:
            html += '<input id="%s" class="switch switch-shadow" type="checkbox" checked="true"/>'
        else:
            html += '<input id="%s" class="switch switch-shadow" type="checkbox"/>'
        html += '<label for="%s"></label>'
        html += '</div>'
        return mark_safe(html)

    def value_from_datadict(self, data, files, name):
        pass