class OpenError(Exception):
    """Raised when the database cannot be opened."""

    pass


class OpenedError(Exception):
    """Raised when the database is already open."""

    pass
