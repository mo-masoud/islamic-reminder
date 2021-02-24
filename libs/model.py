import os
import sqlite3


class Model:
    _db = os.path.join(os.path.dirname(__file__), '../database.db')
    _fillable: {}
    _timestamp: {}
    _fillable_references: {}

    def __init__(self, table):
        self.table = table
        self.connection = sqlite3.connect(self._db)
        self.connection.row_factory = sqlite3.Row
        self.createTable()

    def createTable(self):
        try:
            fillable = {'id': 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'}
            for col, type in self._fillable.items():
                if col != "id": fillable[col] = type

            if self._timestamp:
                fillable['updated_at'] = 'DATETIME DEFAULT CURRENT_TIMESTAMP'
                fillable['created_at'] = 'DATETIME DEFAULT CURRENT_TIMESTAMP'

            for col, table in self._fillable_references.items():
                fillable[f'FOREIGN KEY({col})'] = f'REFERENCES {table}'

            columns = ''
            for col, type in fillable.items():
                columns += col + ' ' + type + ', '

            columns = columns.rstrip(', ')

            sql = 'CREATE TABLE IF NOT EXISTS {}({})'.format(self.table, columns)
            print(sql)
            self.connection.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(e)

    def create(self, row):
        bindings = '('
        keys = '('
        values = []
        i = 0
        for key, value in row.items():
            bindings += '?'
            keys += key
            values.append(value)
            i += 1
            if i != (len(row)):
                bindings += ', '
                keys += ', '
        bindings += ')'
        keys += ')'
        sql = 'INSERT INTO {} {} VALUES {}'.format(self.table, keys, bindings)
        print(sql, values)
        cursor = self.connection.execute(sql, values)
        self.connection.commit()
        return cursor.lastrowid

    def all(self):
        sql = 'SELECT * FROM {}'.format(self.table)
        print(sql)
        cursor = self.connection.execute(sql)
        rows = []
        for row in cursor:
            print(dict(row))
            rows.append(row)
        return rows

    def find(self, column, op, value, order_by='id', order_method='ASC'):
        sql = "SELECT * FROM {} WHERE {} {} '{}' ORDER BY {} {}".format(self.table, column, op, value, order_by, order_method)
        print(sql)
        cursor = self.connection.execute(sql)
        rows = []
        for row in cursor:
            rows.append(dict(row))
        return rows

    def update(self, row, where):
        keys = ''
        values = []
        i = 0
        for key, value in row.items():
            keys += key + ' = ?'
            values.append(value)
            i += 1
            if i != len(row):
                keys += ', '
        sql = 'UPDATE {} SET {} WHERE {} = {}'.format(self.table, keys, where['key'], where['value'])
        print(sql, values)
        self.connection.execute(sql, values)
        self.connection.commit()

    def delete(self, where):
        sql = 'DELETE FROM {} WHERE {} = {}'.format(self.table, where['key'], where['value'])
        print(sql)
        self.connection.execute(sql)
        self.connection.commit()
