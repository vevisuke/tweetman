# -*- coding=utf-8 -*-

import sys
import os
import shutil
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

    def test_write_row_01(self):
        file = 'test/file/tweetman_fdb_write_row_01.txt'
        tmp_file = 'test/file/tweetman_fdb_write_row_01_tmp.txt'
        after_file = 'test/file/tweetman_fdb_write_row_01_after.txt'
        shutil.copyfile(file, tmp_file)
        db = DB(tmp_file)
        id = '1234'
        user = 'testuser'
        text = u'日本語'
        self.assertEqual(db, db.write_row(id, user, text))

        tmp_file_str = open(tmp_file, 'r').read()
        after_file_str = open(after_file, 'r').read()
        self.assertEqual(tmp_file_str, after_file_str)
        os.remove(tmp_file)

    def test_get_latest_row_01(self):
        file = 'test/file/tweetman_fdb_01.txt'
        db = DB(file).load()
        row = db.get_latest_row()
        self.assertEqual('DBRow', row.__class__.__name__)

if __name__ == '__main__':
    unittest.main()
