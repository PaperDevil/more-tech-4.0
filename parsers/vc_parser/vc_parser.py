from typing import List

from parsers.article import Article
from parsers.article_data_source import ArticleDataSource
from parsers.vc_parser import vc_config
from parsers.vc_parser.vc_article_content import VcArticleContent
from parsers.vc_parser.vc_article_parser import VcArticleParser
from parsers.vc_parser.vc_article_urls_extractor import VcArticleUrlsExtractor


class VcParser(ArticleDataSource):

    def get_data(self) -> List[Article]:
        vc_article_urls_extractor = VcArticleUrlsExtractor()
        articles = []
        for tag in vc_config.TAG_LIST:
            article_urls = vc_article_urls_extractor.extract_urls(tag)
            for article_url in article_urls:
                try:
                    vc_article = self.parse_article(article_url)
                    article = Article(title=vc_article.title, text=vc_article.text, tag=tag, date=vc_article.date)
                    articles.append(article)
                except Exception:
                    print("Не удалось распарсить статью " + article_url)

        return articles

    def parse_article(self, article_url) -> VcArticleContent:
        return VcArticleParser().parse_article(article_url)
