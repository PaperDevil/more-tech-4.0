# more-tech-4.0
Код предоставлен командой Vatabe, для участия в хакатоне More Tech 4.0, трек: Data.

# Usage
Requirements:
- Linux (Debian 10, CentOS)
- Docker (20.10.18, build b40c2f6)
- Docker-compose (v2.0.1)
- Kafka (pure Latest)

### Setup configs
For faust_app change config inside `faust_app/app/main.py`
```python
KAFKA_URL = os.getenv('KAFKA_URL', 'kafka://HOST:PORT')

MONGODB_URL = os.getenv('MONGODB_URL', 'MONGO_HOST:PORT')
MONGODB_LOGIN = os.getenv('MONGODB_LOGIN', 'USER')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD', 'PASSWORD')
```

Next setup work of parsers inside `parsers_daemon`:
```python
KAFKA_URL = os.getenv('KAFKA_URL', 'kafka://HOST:PORT')
```

And run it
```shell
 $ screen python buh.py
 $ screen python dataset.py
```

And just run containers
```shell
 $ docker-compose up -d
```

# Demo
API URL - http://85.193.92.92:8000/api/docs#/

Realtime Kafka tracking - http://85.193.92.92:8081/
