from typing import List, Optional

from faust import Record


class PostRecord(Record):
    title: Optional[str] = None
    text: Optional[str] = None
    is_trusted: Optional[bool] = None
    tags: List[str] = []
    source: Optional[str] = None