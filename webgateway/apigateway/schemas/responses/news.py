import typing
from ninja import Schema


class NewsResponse(Schema):
    id: int
    title: typing.Optional[str]
    content: typing.Optional[str]
    short: typing.Optional[str]
    tags: typing.List[str]
    source: typing.Optional[str]
    date: typing.Optional[str]
