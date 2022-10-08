from faust import App, Stream

from db.base import MongoDB
from .models import PostRecord
from .topics import get_post_topic
from .preprocessor import (
    preprocess_post,
)


class FaustApp:
    app: App
    mongo: MongoDB

    def __init__(self, kafka_url: str, mongo_url: str):
        self.app = App(
            'preprocessor',
            version=1,
            broker=kafka_url,
            value_serializer='json',
        )
        self.mongo = MongoDB(mongo_url)

    def listen(self):
        post_topic = get_post_topic(self.app)

        @self.app.agent(post_topic)
        async def consume_posts(stream: Stream):
            async for event in stream.events():
                post: PostRecord = event.value
                preprocessed_post = preprocess_post(
                    post_id=event.key,
                    group_id=post.group_id,
                    location=post.location,
                    post_type=post.post_type,
                    text=post.text,
                    image_link=post.image_link,
                    explicit=post.explicit,
                    tags=post.tags
                )
                await self.mongo.save_post(preprocessed_post)
                # send post id to topic
                yield event.key

        self.app.main()
