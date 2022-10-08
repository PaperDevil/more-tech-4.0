from parsers.article import Article
from parsers.vc_parser.kafka_sender import KafkaSender
from parsers.vc_parser.vc_article_parser import VcArticleParser


class ArticleParserCallback:
    def __init__(self):
        self.kafka_sender = KafkaSender()

    def parse_article(self, article_url: str, tag: str):
        try:
            vc_article = VcArticleParser().parse_article(article_url)
            article = Article(title=vc_article.title, text=vc_article.text, tag=tag, date=vc_article.date)
            self.kafka_sender.send_article_to_kafka(article)
        except Exception:
            print("Не удалось распарсить статью " + article_url)
