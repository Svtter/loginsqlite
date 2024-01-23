import pytest
from loginsqlite import Logger


@pytest.fixture
def db_name():
    import pathlib
    import uuid

    db_name = pathlib.Path(f"temp/{str(uuid.uuid4())}/test.db")
    db_name.parent.mkdir(parents=True, exist_ok=True)
    yield db_name


def test_has_table(db_name):
    logger = Logger(db_name)
    logger.open_db()
    logger.create_table()
    assert logger.has_table()


def test_not_has_table(db_name):
    logger = Logger(db_name)
    logger.open_db()
    assert not logger.has_table()


def test_logger(db_name):
    logger = Logger(db_name)
    logger.open_db()
    logger.create_table()
    logger.info("test")
