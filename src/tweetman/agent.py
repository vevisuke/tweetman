# -*- coding=utf-8 -*-

import ConfigParser
import tweepy
from tweetman.fdb import DB

class Agent:
    def __init__(self, config_file):
        self.config = Config(config_file).parse()
        self.db = DB(self.config.db).load()

    def oauth(self):
        auth = tweepy.OAuthHandler(self.config.consumer_key, self.config.consumer_secret)
        auth.set_access_token(self.config.access_key, self.config.access_secret)
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
