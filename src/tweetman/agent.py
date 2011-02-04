# -*- coding=utf-8 -*-
# Tweetman
# Copyright 2011 vevisuke<vevisuke@gmail.com>
# See LICENSE for details.

import ConfigParser
import tweepy
from tweetman.fdb import DB

class Agent:
    def __init__(self, config_file):
        self.config = Config(config_file)
        self.db = DB(self.config.get('global','db')).load()

    def oauth(self):
        consumer_key = self.config.get('oauth', 'consumer_key')
        consumer_secret = self.config.get('oauth', 'consumer_secret')
        access_key = self.config.get('oauth', 'access_key')
        access_secret = self.config.get('oauth', 'access_secret')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth_handler=auth)
        return self

    def send_direct_message(self, message, to_user):
        return self.api.send_direct_message(user=to_user, text=message)

    def send_direct_messages(self, message, member_list):
        dm_model_list = []
        for user in member_list:
            dm_model_list.append(self.api.send_direct_message(user=user, text=message))

        if len(dm_model_list) == len(member_list):
            return dm_model_list
        else:
            return None


class Config:
    def __init__(self, config_file):
        self.config = ConfigParser.ConfigParser()
        self.config.read(config_file)

    def get(self, section, key):
        return self.config.get(section, key)
