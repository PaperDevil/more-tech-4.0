from time import sleep
from typing import List

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from parsers.vc_parser import vc_config
from parsers.vc_parser.article_parser_callback import ArticleParserCallback
from parsers.vc_parser.vc_config import HUMAN_BEHAVIOR_IMITATION_ENABLED, BASE_URL

import pickle


class VcArticleUrlsExtractor:

    def start_extracting_urls(self, article_parser_callback: ArticleParserCallback):
        browser_map: dict[ChromeDriverManager] = self.__init_browsers()

        article_urls_set = self.__load_processed_urls()
        processed_articles_count = 0
        i = 0
        while True:
            processing_tag = vc_config.TAG_LIST[i]
            print("Обработка тега " + processing_tag)
            print("i = " + str(i))
            self.__sleep_if_need()
            urls = self.__get_urls_from_page(browser_map[processing_tag].page_source)
            for url in urls:
                if not url in article_urls_set:
                    article_urls_set.add(url)
                    article_parser_callback.parse_article(url, processing_tag)

            self.__scroll_to_bottom(browser_map[processing_tag])
            if i == len(vc_config.TAG_LIST) - 1:
                i = 0
            else:
                i += 1

            if processed_articles_count % 50 == 0 and processed_articles_count > 0:
                self.__dump_loaded_articles(article_urls_set)
            processed_articles_count += 1

    def __init_browsers(self) -> dict[ChromeDriverManager]:
        browser_map = dict()
        for tag in vc_config.TAG_LIST:
            browser = webdriver.Chrome(ChromeDriverManager().install())
            browser.get(BASE_URL + tag)
            browser_map[tag] = browser

        return browser_map

    def __get_urls_from_page(self, page_source) -> List[str]:
        soup = BeautifulSoup(page_source, "html.parser")
        articles = soup.findAll('a', class_='content-link')
        urls = []
        for article in articles:
            urls.append(article['href'])

        return urls

    def __scroll_to_bottom(self, browser):
        last_feed_chunk = browser.find_elements(By.CLASS_NAME, "feed__chunk")[-1]
        ActionChains(browser).move_to_element(last_feed_chunk).perform()

    def __sleep_if_need(self):
        if HUMAN_BEHAVIOR_IMITATION_ENABLED:
            sleep(1)

    def __load_processed_urls(self) -> set:
        try:
            with (open("loaded_articles.pickle", "rb")) as pickle_file:
                articles_set = pickle.load(pickle_file)
                return articles_set
        except Exception:
            return set()

    def __dump_loaded_articles(self, articles_set: set):
        f = open('loaded_articles.pickle', 'wb')
        pickle.dump(articles_set, f, protocol=pickle.HIGHEST_PROTOCOL)
        f.close()
