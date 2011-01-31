# -*- coding=utf-8 -*-

import sys
sys.path.append('src')
sys.path.append('src/vender/tweepy')
import unittest
from tweetman.agent import Config

class TestConfig(unittest.TestCase):
    def test_get_01(self):
        config_file = 'test/file/tweetman_config_01.cfg'
        config = Config(config_file)
        self.assertEqual('my_db_file', config.get('global', 'db'))


if __name__ == '__main__':
    unittest.main()
