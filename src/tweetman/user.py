# -*- coding=utf-8 -*-

import csv
import ConfigParser

__version__ = '0.0.1'

class User:
    def __init__(self, config_obj, follower_list=[]):
        self.config = config.obj
        self.follower_list = follower_list
        self.members = self.config.get('global', 'member_list').split()

    def list_remove_list(self):
        send_users = []
        self.follower_list
        self.members

    def get_dm_member_list(self):
        send_users = []
        for follower in self.api.followers():
            if follower.screen_name in self.config.member_list:
                send_users.append(follower.screen_name)
        return send_users


class Config:
    def __init__(self, config_file):
        self.config = ConfigParser.ConfigParser()
        self.config.read(config_file)

    def parse(self):
        self.db = self.config.get('global', 'db')
        self.member_list = self.config.get('global', 'member_list').split()
        self.consumer_key = self.config.get('oauth', 'consumer_key')
        self.consumer_secret = self.config.get('oauth', 'consumer_secret')
        self.access_key = self.config.get('oauth', 'access_key')
        self.access_secret = self.config.get('oauth', 'access_secret')
        return self


