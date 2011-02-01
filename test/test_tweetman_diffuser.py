# -*- coding=utf-8 -*-

import sys
sys.path.append('src')
sys.path.append('src/vender/tweepy')
import unittest
from tweetman.diffuser import Message, DirectMessage

class DMMock:
    def __init__(self):
        self.id = 1111
        self.sender = SenderMock()
        self.text = 'this_is_mock'


class SenderMock:
    def __init__(self):
        self.screen_name = 'mock_user'


class TestDirectMessage(unittest.TestCase):
    def test_new_01(self):
        mock = DMMock()
        dm = DirectMessage(mock)
        self.assertEqual(mock.id, dm.id)
        self.assertEqual(mock.sender.screen_name, dm.sender)
        self.assertEqual(mock.text, dm.text)

    def test_create_cc_direct_message_01(self):
        mock = DMMock()
        dm = DirectMessage(mock)
        text = u'[from mock_user] this_is_mock'
        self.assertEqual(text, dm.create_cc_direct_message())

    def test_create_cc_direct_message_notice_01(self):
        mock = DMMock()
        dm = DirectMessage(mock)
        members = ['to1', 'to2']
        text = u'to1 to2に以下のDMを送信しました。this_is_mock'
        self.assertEqual(text, dm.create_cc_direct_message_notice(members))


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

if __name__ == '__main__':
    unittest.main()
