from dataclasses import dataclass


@dataclass
class Log(object):
    level: str
    datetime: int
    msg: str
