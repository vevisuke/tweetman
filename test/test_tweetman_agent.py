# -*- coding=utf-8 -*-

import sys
sys.path.append('src')
sys.path.append('src/vender/tweepy')
import unittest
from tweetman.agent import Config
from tweetman.agent import Agent

class TestAgent(unittest.TestCase):
    def test_new_01(self):
        config_file = 'test/file/tweetman_agent_01.cfg'
        agent = Agent(config_file)
        self.assertEqual('Config', agent.config.__class__.__name__)

class TestConfig(unittest.TestCase):
    def test_get_01(self):
        config_file = 'test/file/tweetman_config_01.cfg'
        config = Config(config_file)
        self.assertEqual('my_db_file', config.get('global', 'db'))


if __name__ == '__main__':
    unittest.main()
