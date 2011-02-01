# -*- coding=utf-8 -*-

import sys
sys.path.append('src')
sys.path.append('src/vender/tweepy')
import unittest
from tweetman.diffuser import DirectMessage

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

if __name__ == '__main__':
    unittest.main()
