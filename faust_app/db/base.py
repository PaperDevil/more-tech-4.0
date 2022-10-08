from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection
from pymongo.database import Database


class MongoDB:
    _db: Database
    _users: Collection
    _posts: Collection
    _interactions: Collection

    def __init__(self, connection_string):
        client = AsyncIOMotorClient(connection_string)
        self._db = client.feature_store

        self._users = self._db.users
        self._users.create_index('user_id')

        self._posts = self._db.posts
        self._posts.create_index('post_id')

        self._interactions = self._db.interactions

    def save_post(self, post: dict):
        id = self._posts.insert_one(post)
        return id
