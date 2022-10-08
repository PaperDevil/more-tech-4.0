import typing
from ninja import Schema


class PageSchema(Schema):
    limit: typing.Optional[int]
    offset: typing.Optional[int]
