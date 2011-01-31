# -*- coding=utf-8 -*-

import sys
sys.path.append('src')
sys.path.append('src/vender/tweepy')
import unittest
from tweetman.agent import Message
from tweetman.agent import Config

class TestMessage(unittest.TestCase):
    def test_get_140str_01(self):
        str = ''
        tweet = Message(str)
        self.assertEqual(str, str)

    def test_create_cc_direct_message_01(self):
        str = u'おはよう'
        from_user_name = 'fromexample'
        tweet = Message(str)
        return_dm = tweet.create_cc_direct_message(from_user_name)
        dm = u'[from fromexample] おはよう'
        self.assertEqual(dm, return_dm)

    def test_create_cc_direct_message_notice_01(self):
        str = u'おはよう'
        dm_user = ['to', 'to2', 'to3']
        tweet = Message(str)
        return_dm = tweet.create_cc_direct_message_notice(dm_user)
        dm = u'to to2 to3に以下のDMを送信しました。おはよう'
        self.assertEqual(dm, return_dm)

class TestConfig(unittest.TestCase):
    def test_get_01(self):
        config_file = 'test/file/tweetman_config_01.cfg'
        config = Config(config_file)
        self.assertEqual('my_db_file', config.get('global', 'db'))


if __name__ == '__main__':
    unittest.main()
