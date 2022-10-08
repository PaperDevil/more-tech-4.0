import requests
from bs4 import BeautifulSoup
import datetime

from parsers.vc_parser.vc_article_content import VcArticleContent


class VcArticleParser:
    def parse_article(self, article_url) -> VcArticleContent:
        page = requests.get(article_url)
        soup = BeautifulSoup(page.text, "html.parser")
        title = soup.h1.text
        content_full = soup.find_all('div', class_="content content--full")
        islands = content_full[0].find_all("div", class_="l-island-a")
        text = ""
        for island in islands:
            text = text + island.text

        date = self.__extract_date(soup)
        return VcArticleContent(title, text, date)

    def __extract_date(self, soup: BeautifulSoup) -> str:
        time_in_millis = int(soup.find_all('time', class_="time")[1]['data-date'])
        time = datetime.datetime.fromtimestamp(time_in_millis)
        date = time.strftime("%Y/%m/%d")
        return date


if __name__ == "__main__":
    parser = VcArticleParser()
    content = parser.parse_article(
        "https://vc.ru/tech/508662-android-13-poluchat-11-telefonov-ot-samsung-odin-iz-nih-v-etom-spiske-ne-zhdali")
    print(content.text)
    print("----")
    print(content.title)
