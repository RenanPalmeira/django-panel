from __future__ import unicode_literals

from tweepy import OAuthHandler

TWITTER_API_KET = 'BrIw1uaHiwtLuMR4fPEdZvWIn'
TWITTER_API_SECRET = 'ElACMUj36nvrwTWtwlQthvjVsmNF3u42k4hEsO2Puqv0mVtl23'

TwitterProvider = OAuthHandler(TWITTER_API_KET, TWITTER_API_SECRET)