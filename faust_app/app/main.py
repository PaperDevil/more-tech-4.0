import os

from .app import FaustApp

KAFKA_URL = os.getenv('KAFKA_URL', 'kafka://185.104.112.241:9093')

MONGODB_URL = os.getenv('MONGODB_URL', '185.104.112.241:27017')
MONGODB_LOGIN = os.getenv('MONGODB_LOGIN', 'mongosir')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD', 'mongopass')

MONGO_URL = f'mongodb://{MONGODB_LOGIN}:{MONGODB_PASSWORD}@{MONGODB_URL}'

faust_app = FaustApp(KAFKA_URL, MONGO_URL)