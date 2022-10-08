from typing import List, Optional

from faust import Record


class PostRecord(Record):
    title: Optional[str] = None
    content: Optional[str] = None
    is_trusted: Optional[bool] = None
    tags: List[str] = []
    source: Optional[str] = None
    date: Optional[str] = None