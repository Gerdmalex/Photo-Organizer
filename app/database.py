from sqlite3 import connect


class Database:
    def __init__(self):
        self.db = connect(":memory:")
        cur = self.db.cursor()
        cur.execute('''CREATE TABLE files (path TEXT, name TEXT, date TEXT, time TEXT)''')
        self.db.commit()

    def insert(self, *args):
        cur = self.db.cursor()
        cur.execute("INSERT INTO files VALUES (?, ?, ?, ?)", args)
        self.db.commit()

    def read(self):
        cur = self.db.cursor()
        return list(cur.execute("SELECT * FROM files ORDER BY date, time"))

    def close(self):
        self.db.close()


