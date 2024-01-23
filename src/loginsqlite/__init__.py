import sqlite3
from typing import Optional
from . import err


class Logger:
    def __init__(self, filename: str):
        self.filename = filename
        self.file = None
        self.con: Optional[sqlite3.Connection] = None

    def open_db(self):
        if not self.con:
            self.con = sqlite3.connect(self.filename)
        else:
            raise err.OpenedError("sqlite3 database already open")

    def init_db(self):
        """first run dbfile"""
        self.open_db()
        self.create_table()

    def close_db(self):
        if self.con:
            self.con = None
        else:
            raise err.OpenError("sqlite3 database not open")

    def get_cursor(self):
        """promised get cursor"""
        if self.con:
            return self.con.cursor()
        else:
            raise err.OpenError("sqlite3 database not open")

    def commit_db(self):
        if self.con:
            self.con.commit()
        else:
            raise err.OpenError("sqlite3 database not open")

    def create_table(self):
        cur = self.get_cursor()
        cur.execute("CREATE TABLE log(datetime, level, msg)")
        self.commit_db()

    def get_handler(self):
        """handler for logging library"""
        pass

    def has_table(self) -> bool:
        cur = self.get_cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='log';")
        res = cur.fetchone()
        return res is not None

    def info(self, msg):
        from datetime import datetime

        if not self.has_table():
            self.create_table()

        if not isinstance(msg, str):
            raise TypeError("msg must be a string")

        current_time = datetime.now()
        cur = self.get_cursor()
        cur.execute(
            f"""
            INSERT INTO log values
            ("{current_time}","INFO", "{msg}")
        """
        )

        self.commit_db()


def get_default() -> Logger:
    return Logger("temp.db")
