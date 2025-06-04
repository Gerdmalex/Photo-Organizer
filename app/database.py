from sqlite3 import connect


class Database:
    """
    A class representing a database for operations with information about files.
    """
    def __init__(self):
        """
        Creates connection to the SQLite and creates tables.
        """
        self.db = connect(":memory:")
        cur = self.db.cursor()
        cur.execute('''CREATE TABLE files (path TEXT, name TEXT, date TEXT, time TEXT)''')
        self.db.commit()

    def insert(self, *args):
        """
        Inserting data into the database.

        Arbitrary arguments args:
            path (str): The path to a file in the file system.
            name (str): The name of the file.
            date (str): File creation date.
            time (str): File creation time.
        """
        cur = self.db.cursor()
        cur.execute("INSERT INTO files VALUES (?, ?, ?, ?)", args)
        self.db.commit()

    def read(self):
        """
        Get all datasets from the database.

        Returns:
            list: List of all datasets stored in the database.
        """
        cur = self.db.cursor()
        return cur.execute("SELECT * FROM files ORDER BY date, time, name").fetchall()

    def count(self):
        """
        The count of datasets stored in the database.

        Returns:
            int: Count of datasets.
        """
        cur = self.db.cursor()
        return cur.execute("SELECT COUNT(*) FROM files").fetchone()[0]

    def close(self):
        """
        Close the database connection.
        """
        self.db.close()


