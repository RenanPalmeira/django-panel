from __future__ import unicode_literals

from django.conf import settings
from tweepy import OAuthHandler

TWITTER_API_KET =  settings.TWITTER_API_KET
TWITTER_API_SECRET = settings.TWITTER_API_SECRET

TwitterProvider = OAuthHandler(TWITTER_API_KET, TWITTER_API_SECRET)