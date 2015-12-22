from __future__ import unicode_literals

from django.conf import settings
from tweepy import OAuthHandler, API

TWITTER_API_KEY =  settings.TWITTER_API_KEY
TWITTER_API_SECRET = settings.TWITTER_API_SECRET

TwitterProvider = OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)