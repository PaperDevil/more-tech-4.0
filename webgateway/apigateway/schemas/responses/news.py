import typing
from ninja import Schema


class NewsResponse(Schema):
    _id: str
    title: typing.Optional[str]
    content: typing.Optional[str]
    short: typing.Optional[str]
    tags: typing.Any
    source: typing.Optional[str]
    date: typing.Optional[str]
    is_trusted: typing.Optional[str]
