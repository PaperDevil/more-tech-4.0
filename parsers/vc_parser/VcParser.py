from typing import List

from parsers.Article import Article
from parsers.ArticleDataSource import ArticleDataSource
from parsers.vc_parser import VcConfig
from parsers.vc_parser.VcArticleContent import VcArticleContent
from parsers.vc_parser.VcArticleParser import VcArticleParser
from parsers.vc_parser.VcArticleUrlsExtractor import VcArticleUrlsExtractor


class VcParser(ArticleDataSource):

    def get_data(self) -> List[Article]:
        vc_article_urls_extractor = VcArticleUrlsExtractor()
        articles = []
        for tag in VcConfig.TAG_LIST:
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
