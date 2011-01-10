# -*- coding=utf-8 -*-

import sys
import unittest

sys.path.append('lib/')
from tweetdiffuser import TweetString
from tweetdiffuser import TweetDB
from tweetdiffuser import TweetDiffuser
from tweetdiffuser import Config

class TestTweetDiffuser(unittest.TestCase):
    def test_new_01(self):
        config_file = 'test/file/diffuser_new_01.conf'
        diffuser = TweetDiffuser(config_file)
        self.assertEqual('TweetDB', diffuser.db.__class__.__name__)
        self.assertEqual('Config', diffuser.config.__class__.__name__)

class TestConfig(unittest.TestCase):
    def test_new_01(self):
        config_file = 'test/file/config_new_01.conf'
        config = Config(config_file)
        self.assertEqual(config, config.parse())
        self.assertEqual(['to1', 'to2', 'to3', 'to4'], config.member_list)

class TestTweetString(unittest.TestCase):
    def test_get_140str_01(self):
        str = ''
        tweet = TweetString(str)
        self.assertEqual(str, str)

    def test_create_cc_direct_message_01(self):
        str = u'おはよう'
        from_user_name = 'fromexample'
        tweet = TweetString(str)
        return_dm = tweet.create_cc_direct_message(from_user_name)
        dm = u'[from fromexample] おはよう'
        self.assertEqual(dm, return_dm)

    def test_create_cc_direct_message_notice_01(self):
        str = u'おはよう'
        dm_user = ['to', 'to2', 'to3']
        tweet = TweetString(str)
        return_dm = tweet.create_cc_direct_message_notice(dm_user)
        dm = u'to to2 to3に以下のDMを送信しました。おはよう'
        self.assertEqual(dm, return_dm)


class TestTweetDB(unittest.TestCase):
    def test_load_01(self):
        file = 'test/file/tweetdb_load_01.txt'
        db = TweetDB(file)
        self.assertEqual(db, db.load())
        self.assertEqual(2, len(db.rows))
        self.assertEqual('TweetDBRow', db.rows[0].__class__.__name__)
        self.assertEqual('TweetDBRow', db.rows[1].__class__.__name__)

        self.assertEqual('1111', db.rows[0].id)
        self.assertEqual('exampleid', db.rows[0].user)
        self.assertEqual('This is sample tweet.', db.rows[0].text)

        self.assertEqual('2222', db.rows[1].id)
        self.assertEqual('exampleid2', db.rows[1].user)
        self.assertEqual('This is 日本語 tweet.', db.rows[1].text)

    def test_add_row_01(self):
        file = 'test/file/tweetdb_add_row_01.txt'
        id = '3333'
        user = 'example'
        text = 'Hello world'
        db = TweetDB(file)
        db.load()
        self.assertEqual(db, db.add_row(id, user, text))


if __name__ == '__main__':
    unittest.main()
