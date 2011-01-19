# -*- coding=utf-8 -*-

import sys
from optparse import OptionParser

sys.path.append('lib/')
sys.path.append('vender/tweepy/')
from tweetdiffuser import TweetDiffuser

parser = OptionParser()
parser.add_option("-c", "--config", dest="configfile",
                  help="config file")
(options, args) = parser.parse_args()

if options.configfile is None: sys.exit(1)

diffuser = TweetDiffuser(options.configfile)
diffuser.oauth()
diffuser.diffuse()
