from faust import App, TopicT
from faust.types import ModelArg

from app.models import PostRecord


class Topic:
    topic: TopicT

    def __init__(self, app: App, name: str, key_type: ModelArg = int, value_type: ModelArg = None):
        self.topic = app.topic(name, key_type=key_type, value_type=value_type)


def get_post_topic(app: App) -> TopicT:
    return Topic(app, 'posts', value_type=PostRecord).topic
