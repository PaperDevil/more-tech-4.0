import json
import os

from kafka import KafkaProducer

from parsers.article import Article
from parsers.vc_parser.vc_parser import VcParser

KAFKA_URL = os.getenv('KAFKA_URL', '127.0.0.1:9093')
producer = KafkaProducer(bootstrap_servers=[KAFKA_URL],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def send_article_to_kafka(article_to_send: Article):
    article_for_kafka = {
        'title': article_to_send.title,
        'content': article_to_send.text,
        'tags': article_to_send.tag,
        'source': 'vc.ru',
        'date': article_to_send.date
    }
    producer.send('posts', article_for_kafka)


if __name__ == '__main__':
    articles = VcParser().get_data()
    for article in articles:
        send_article_to_kafka(article)
        print(article)
        print("---" * 30)
