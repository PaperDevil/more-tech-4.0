from parsers.article_data_source import ArticleDataSource
from parsers.vc_parser.article_parser_callback import ArticleParserCallback
from parsers.vc_parser.vc_article_urls_extractor import VcArticleUrlsExtractor


class VcParser(ArticleDataSource):

    def start_parsing(self):
        VcArticleUrlsExtractor().start_extracting_urls(ArticleParserCallback())


# Запустить парсинг
if __name__ == '__main__':
    VcParser().start_parsing()
