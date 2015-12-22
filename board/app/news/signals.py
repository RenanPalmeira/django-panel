from __future__ import unicode_literals, absolute_import

import logging

logger = logging.getLogger(__name__)

from django.dispatch import receiver
from django.db.models.signals import post_save

from board.core.provider.twitter import TwitterProvider, API

from .models import Article

@receiver(post_save, sender=Article)
def article_post_save(sender, instance, **kwargs):
	if 'account' in dir(instance):
		user = instance.account
		social = user.social_set.select_related().first()
		try:
			if social:
				TwitterProvider.set_access_token(social.token, social.secret)
				api = API(TwitterProvider)
				api.update_status(instance.title)
		except Exception, e:
			logger.warning(e)
			
		
