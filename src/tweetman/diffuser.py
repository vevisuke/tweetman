# -*- coding=utf-8 -*-

from tweetman.agent import Agent

class Diffuser(Agent):
    def diffuse(self):
        sent_dm_list = []
        latest_id = self.db.get_latest_row().id if self.db.get_latest_row() else 0
        dm_list = self.api.direct_messages(since_id=latest_id)
        for dm in dm_list:
            tweet_str = Message(dm.text)
            message = tweet_str.create_cc_direct_message(dm.sender.screen_name)
            sent_dm_list.append(self.send_direct_messages(message, self.get_dm_member_list()))

            notice = tweet_str.create_cc_direct_message_notice(self.get_dm_member_list())
            self.send_direct_message(notice, dm.sender.screen_name)

            self.db.add_row(dm.id, dm.sender.screen_name, '')
        print sent_dm_list
        if len(sent_dm_list) == len(dm_list):
            return True
        else:
            return False

    def get_dm_member_list(self):
        send_users = []
        for follower in self.api.followers():
            if follower.screen_name in self.config.member_list:
                send_users.append(follower.screen_name)
        return send_users


class Message:
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
