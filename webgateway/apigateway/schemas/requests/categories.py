import typing
from ninja import Schema


class CategoriesSchema(Schema):
    categories: typing.List[str]