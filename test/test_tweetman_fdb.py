# -*- coding=utf-8 -*-

import sys
sys.path.append('src')
import unittest
from tweetman.fdb import DB

class TestDB(unittest.TestCase):
    def test_new_01(self):
        file = 'nofile'
        db = DB(file)
        self.assertEqual(file, db.file)

    def test_load_01(self):
        file = 'test/file/tweetman_fdb_01.txt'
        db = DB(file)
        self.assertEqual(db, db.load())

    def test_get_latest_row_01(self):
        file = 'test/file/tweetman_fdb_01.txt'
        db = DB(file).load()
        row = db.get_latest_row()
        self.assertEqual('DBRow', row.__class__.__name__)

if __name__ == '__main__':
    unittest.main()
