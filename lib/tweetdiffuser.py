# -*- coding=utf-8 -*-

import sys
sys.path.append('vender/tweepy/')

import csv
import ConfigParser
import tweepy

__version__ = '0.0.1'

class TweetDiffuser:
    def __init__(self, config_file):
        self.config = Config(config_file).parse()
        self.db = TweetDB(self.config.db).load()

    def oauth(self):
        auth = tweepy.OAuthHandler(self.config.consumer_key, self.config.consumer_secret)
        auth.set_access_token(self.config.access_key, self.config.access_secret)
        self.api = tweepy.API(auth_handler=auth)
        return self

    def send_direct_messages(self, message, member_list):
        for user in member_list:
            self.api.send_direct_message(user=user, text=message)
        return True

    def send_direct_message(self, message, to_user):
        self.api.send_direct_message(user=to_user, text=message)
        return True

    def diffuse(self):
        latest_id = self.db.get_latest_row().id if self.db.get_latest_row() else 0
        dm_list = self.api.direct_messages(since_id=latest_id)
        for dm in dm_list:
            tweet_str = TweetString(dm.text)
            message = tweet_str.create_cc_direct_message(dm.sender.screen_name)
            self.send_direct_messages(message, self.get_dm_member_list())

            notice = tweet_str.create_cc_direct_message_notice(self.get_dm_member_list())
            self.send_direct_message(notice, dm.sender.screen_name)

            self.db.add_row(dm.id, dm.sender.screen_name, '')
        return True

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


class TweetString:
    def __init__(self, str):
        self.original_tweet = str

    def get_140str(self, string):
        return string[0:139]

    def create_cc_direct_message(self, from_user_name):
        message = '[from ' + from_user_name +  '] ' + self.original_tweet
        return self.get_140str(message)

    def create_cc_direct_message_notice(self, dm_user_list):
        message =  ' '.join(dm_user_list) + u'に以下のDMを送信しました。' + self.original_tweet
        return self.get_140str(message)


class TweetDB:
    def __init__(self, file):
        self.rows = []
        self.file = file
        self.delimiter = '\t'
        self.dialect = 'tsv'
        self.lineterminator = '\n'

    def load(self):
        csv.register_dialect(self.dialect, delimiter=self.delimiter, quoting=csv.QUOTE_NONE)
        reader = csv.reader(open(self.file, 'r'), self.dialect)
        for row in reader:
            self.rows.append(TweetDBRow(row))
        return self

    def add_row(self, id, user, text):
        writer = csv.writer(open(self.file,'a'), self.dialect, lineterminator=self.lineterminator)
        writer.writerow([id, user, text])
        return self

    def get_latest_row(self):
        current_id = 0
        if len(self.rows) == 0: return None
        latest_row = self.rows[0]
        for row in self.rows:
            if int(row.id) > int(current_id):
                current_id = row.id
                latest_row = row
        return latest_row


class TweetDBRow:
    def __init__(self, ary):
        self.id = ary[0]
        self.user = ary[1]
        self.text = ary[2]

