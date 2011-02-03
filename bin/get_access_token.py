# -*- coding: utf-8 -*-

import sys
sys.path.append('src/vender/tweepy')
import tweepy

consumer_key = raw_input("consumer key:")
consumer_secret = raw_input("consumer secret:")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
print "Please access and get verifier code."
print auth.get_authorization_url()

verifier = raw_input("Verifier: ")
auth.get_access_token(verifier)

access_key = auth.access_token.key
access_secret = auth.access_token.secret

print "access token key: " + access_key
print "access token secret: " + access_secret
