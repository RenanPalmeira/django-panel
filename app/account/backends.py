from __future__ import unicode_literals

from .models import Account

class AccountBackend(object):

    def authenticate(self, email=None, password=None):
        try:
            user = Account.objects.get(email = email)
            if user.check_password(password):
                return user
        except Account.DoesNotExist:
            return None
        return None

    def get_user(self, account_id):
        try:
            return Account.objects.get(pk=account_id)
        except Account.DoesNotExist:
            return None