# -*- coding=utf-8 -*-

import sys
sys.path.append('lib/')
sys.path.append('vender/tweepy/')
from tweetdiffuser import TweetDiffuser

config_file = sys.argv[1]
diffuser = TweetDiffuser(config_file)
diffuser.oauth()
diffuser.diffuse()
