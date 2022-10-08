import os
import csv
import time
import json
from urllib.parse import urlparse
from kafka import KafkaProducer
import pendulum


KAFKA_URL = os.getenv('KAFKA_URL', '127.0.0.1:9093')
producer = KafkaProducer(bootstrap_servers=[KAFKA_URL],
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))

dataset = open('dataset.tsv', 'r+')
reader = csv.reader(dataset, delimiter="\t")


i = 0
for line in reader:
    if i == 0:
        i += 1
        continue
    result = {
        'title': line[3],
        'content': line[2],
        'short': None,
        'tags': [],
        'source': urlparse(line[1]).netloc,
        'date': line[0].split(' ')[0].replace('-', '/')
    }
    print(result)
    future = producer.send('posts', result)
    result = future.get(timeout=60)
    i += 1
