# -*- coding=utf-8 -*-

import sys
from optparse import OptionParser

sys.path.append('src/')
sys.path.append('src/vender/tweepy/')
from tweetman.diffuser import Diffuser

parser = OptionParser()
parser.add_option("-c", "--config", dest="configfile",
                  help="config file")
(options, args) = parser.parse_args()

if options.configfile is None: sys.exit(1)

diffuser = Diffuser(options.configfile)
diffuser.oauth()
diffuser.diffuse()
