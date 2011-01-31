# -*- coding=utf-8 -*-

import csv

class DB:
    def __init__(self, file):
        self.rows = []
        self.file = file
        self.delimiter = '\t'
        self.dialect = 'tsv'
        self.lineterminator = '\n'

    def load(self):
        csv.register_dialect(self.dialect, delimiter=self.delimiter, quoting=csv.QUOTE_NONE)
        reader = csv.reader(open(self.file, 'r'), self.dialect)
        for row in reader:
            self.rows.append(DBRow(row))
        return self

    def write_row(self, id, user, text):
        writer = csv.writer(open(self.file,'a'), self.dialect, lineterminator=self.lineterminator)
        writer.writerow([id, user, text])
        return self

    def get_latest_row(self):
        current_id = 0
        if len(self.rows) == 0: return None
        latest_row = self.rows[0]
        for row in self.rows:
            if int(row.id) > int(current_id):
                current_id = row.id
                latest_row = row
        return latest_row

class DBRow:
    def __init__(self, ary):
        self.id = ary[0]
        self.user = ary[1]
        self.text = ary[2]
