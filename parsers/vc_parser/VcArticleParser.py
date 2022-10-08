import requests
from bs4 import BeautifulSoup

from vc_parser.VcArticleContent import VcArticleContent


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

        return VcArticleContent(title, text)


if __name__ == "__main__":
    parser = VcArticleParser()
    content = parser.parse_article(
        "https://vc.ru/finance/515044-bolee-45-tysyach-rossiyan-otkryli-scheta-v-bankah-gruzii-k-oseni-2022-goda")
    print(content.text)
    print("----")
    print(content.title)
