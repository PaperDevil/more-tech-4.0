import json
import os

from kafka import KafkaProducer

from parsers.article import Article

KAFKA_URL = os.getenv('KAFKA_URL', '127.0.0.1:9093')
producer = KafkaProducer(bootstrap_servers=[KAFKA_URL],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


class KafkaSender:
    def send_article_to_kafka(self, article_to_send: Article):
        article_for_kafka = {
            'title': article_to_send.title,
            'content': article_to_send.text,
            'tags': article_to_send.tag,
            'source': 'vc.ru',
            'date': article_to_send.date
        }
        producer.send('posts', article_for_kafka)
