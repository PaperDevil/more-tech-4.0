from datetime import datetime

from bs4 import BeautifulSoup
import time
from selenium import webdriver
import pendulum

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
    command_executor='http://185.104.112.241:4444',
    options=options
)

class ConsulParser:
    URL = 'http://www.consultant.ru'

    def buh_ru(self, duration: pendulum.Duration) -> list:
        result = []
        now = pendulum.now('Europe/Moscow')
        checkpoint = now
        while now > (checkpoint - duration):
            RURL = f'{self.URL}/legalnews/chronomap/{now.year}/{now.month}/'
            driver.get(RURL)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            container = soup.find('div', class_='archive-month__listing')
            for article in container.find_all('div', class_='archive-month__item'):
                title = article.find('span').text
                href = article.find('a').get('href')
                tags = article.get('data-tags')
                date = self.__extract_date(article)
                result.append({
                    'title': title,
                    'href': href,
                    'tags': tags,
                    'date': date
                })
            time.sleep(15)
            now = now - pendulum.duration(months=1)
        return result

    def __extract_date(self, article) -> str:
        iso_date = article.get("data-published-at")
        return datetime.fromisoformat(iso_date).strftime("%Y/%m/%d")


def main():
    parser = ConsulParser()
    a = parser.buh_ru(pendulum.duration(months=1))
    for i in a:
        print(i)


if __name__ == '__main__':
    main()
    driver.quit()
