import json
import os

from bs4 import BeautifulSoup
import requests
import time
from kafka import KafkaProducer

KAFKA_URL = os.getenv('KAFKA_URL', '127.0.0.1:9093')


class BUHParser:
    URL = 'https://buh.ru/rss/?chanel=news'

    #  парсинг сайта ведомостей
    def buh_ru(self, pages: int) -> list:
        result = []
        for i in range(0, pages):
            page = requests.get(
                f'https://buh.ru/news/uchet_nalogi/?PAGEN_1={i}')
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, 'html.parser')
                text_data = soup.find_all('article',
                                          class_='article')
                for article in text_data:
                    title = article.find('a').text
                    href = article.find('a').get('href')
                    short = article.find_all('p')[1].text
                    content = self.get_buh_content(f'https://buh.ru{href}')
                    result.append({
                        'title': title,
                        'content': content,
                        'short': short,
                        'tags': ['accounting', 'finance']
                    })
                time.sleep(3)
            else:
                print('pizda')
        return result

    def get_buh_content(self, link):
        page = requests.get(link)
        soup = BeautifulSoup(page.text, 'html.parser')
        data = soup.find('div', itemprop='articleBody').contents
        content = ''
        for i in data:
            content += i.text
        return content


def main():
    parser = BUHParser()
    data_list = parser.buh_ru(2)
    producer = KafkaProducer(bootstrap_servers=[KAFKA_URL], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    for i in data_list:
        print(i)
        future = producer.send('posts', i)
        result = future.get(timeout=60)

if __name__ == '__main__':
    main()
