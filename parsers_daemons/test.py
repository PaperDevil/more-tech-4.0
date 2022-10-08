# set up producer
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=["127.0.0.1:9093"])
future = producer.send("posts", key=b"my_key", value=b"my_value", partition=0)
result = future.get(timeout=10)
print(result)
