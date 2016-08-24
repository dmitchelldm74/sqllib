import sqlite3
class SQL():
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.c = self.conn.cursor()
        # tname == tablename
    def __del__(self):
        self.conn.close()
    def insert(self, tname, values, *args):
        values = ','.join(values)
        if len(args) > 0:
            self.c.execute('INSERT INTO ' + tname + ' VALUES (' + values + ')', args)
        else:
            self.c.execute('INSERT INTO ' + tname + ' VALUES (' + values + ')')
        self.conn.commit()
    def create(self, tname, *args):
        arg = []
        for a in args:
            arg.append(' '.join(a))
        arg = ','.join(arg)
        print arg
        self.c.execute('CREATE TABLE ' + tname + ' (' + arg + ')')
    def select(self, columns, tname, where, *args):
        columns = ','.join(columns)
        if where != None:
            if len(args) > 0:
                return self.c.execute('SELECT ' + columns + ' FROM ' + tname + ' WHERE ' + where, args)
            return self.c.execute('SELECT ' + columns + ' FROM ' + tname + ' WHERE ' + where)
        return self.c.execute('SELECT ' + columns + ' FROM ' + tname)
    def delete(self, columns, tname, where, *args):
        columns = ','.join(columns)
        if where != None:
            if len(args) > 0:
                self.c.execute('DELETE ' + columns + ' FROM ' + tname + ' WHERE ' + where, args)
            self.c.execute('DELETE ' + columns + ' FROM ' + tname + ' WHERE ' + where)
        self.c.execute('DELETE ' + columns + ' FROM ' + tname)
    def execute(self, to_execute, *args):
        self.c.execute(to_execute, args)
    def remove(self, tname):
        self.c.execute('DROP TABLE ' + tname)
    def exists(self, tname):
        try:
            self.c.execute('SELECT * FROM ' + tname)
            return True
        except:
            return False
