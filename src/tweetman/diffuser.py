# -*- coding=utf-8 -*-

from tweetman.agent import Agent

class Diffuser(Agent):
    def diffuse(self):
        sent_dm_list = []
        latest_id = self.db.get_latest_row().id if self.db.get_latest_row() else 0
        dm_list = self.api.direct_messages(since_id=latest_id)

        for dm in dm_list:
            sent_dm_list.append(self._send_dm(dm))
            self._send_dm_notice(dm)
            self.db.write_row(dm.id, dm.sender.screen_name, dm.text)

        if len(sent_dm_list) == len(dm_list):
            return True
        else:
            return False

    def _send_dm(self, dm):
        message = DirectMessage(dm)
        text = message.create_cc_direct_message()
        return self.send_direct_messages(text, self.get_dm_member_list(message.sender))

    def _send_dm_notice(self, dm):
        message = DirectMessage(dm)
        text = message.create_cc_direct_message_notice(self.get_dm_member_list())
        return self.send_direct_message(text, message.sender)

    def get_dm_member_list(self, ignore=None):
        send_users = []
        for follower in self.api.followers():
            if follower.screen_name == ignore:
                pass
            elif follower.screen_name in self.config.get('global', 'member_list'):
                send_users.append(follower.screen_name)
        return send_users


class DirectMessage:
    def __init__(self, dm):
        self.original_dm = dm
        self.id = dm.id
        self.sender = dm.sender.screen_name
        self.text = dm.text

    def get_140str(self, string):
        return string[0:139]

    def create_cc_direct_message(self):
        message = '[from ' + self.sender +  '] ' + self.text
        return self.get_140str(message)

    def create_cc_direct_message_notice(self, dm_user_list):
        message =  ' '.join(dm_user_list) + u'に以下のDMを送信しました。' + self.text
        return self.get_140str(message)
