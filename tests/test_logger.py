from loginsqlite import Logger


def test_logger():
    l = Logger("temp.db")
    l.info("test")
