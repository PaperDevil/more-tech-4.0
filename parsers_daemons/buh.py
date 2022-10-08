import json
import os
from datetime import datetime

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
        producer = KafkaProducer(bootstrap_servers=[KAFKA_URL],
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        for i in range(0, pages):
            page = requests.get(
                f'https://buh.ru/news/uchet_nalogi/?PAGEN_1={i}')
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, 'html.parser')
                text_data = soup.find_all('article',
                                          class_='article')

                page_date = self.__extract_date_for_page(text_data)
                for article in text_data:
                    try:
                        title = article.find('a').text
                        href = article.find('a').get('href')
                        short = article.find_all('p')[1].text
                        content = self.get_buh_content(f'https://buh.ru{href}')
                        result = {
                            'title': title,
                            'content': content,
                            'short': short,
                            'tags': ['accounting', 'finance'],
                            'source': 'buh.ru',
                            'date': page_date
                        }
                        print(result)
                        future = producer.send('posts', result)
                        result = future.get(timeout=60)
                    except Exception:
                        continue
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

    def __extract_date_for_page(self, text_data) -> str:
        href = text_data[0].find('a').get('href')
        article_url = f'https://buh.ru{href}'
        page = requests.get(article_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        date_str = soup.find_all("span", class_="grayd")[0].text
        time = datetime.strptime(date_str, "%d.%m.%Y")
        date = time.strftime("%Y/%m/%d")
        return date


def main():
    parser = BUHParser()
    data_list = parser.buh_ru(2680)


if __name__ == '__main__':
    main()
