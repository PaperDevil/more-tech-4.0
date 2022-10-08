from typing import List

from faust import Record


class PostRecord(Record):
    title: str
    text: str
    is_trusted: bool
    tags: List[str]
    source: str