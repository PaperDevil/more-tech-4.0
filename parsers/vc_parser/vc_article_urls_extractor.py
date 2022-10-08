from time import sleep
from typing import List

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains

from parsers.vc_parser import vc_config
from parsers.vc_parser.vc_config import ARTICLE_COUNT_TO_PARSE, HUMAN_BEHAVIOR_IMITATION_ENABLED, BASE_URL


class VcArticleUrlsExtractor:

    def extract_urls(self, tag: str):
        return self.__parse_tag(tag)

    def __parse_tag(self, tag: str):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(BASE_URL + tag)

        articles_set = set()
        while len(articles_set) < ARTICLE_COUNT_TO_PARSE:
            self.__sleep_if_need()
            urls = self.__get_url_from_page(browser.page_source)
            for url in urls:
                articles_set.add(url)

            self.__scroll_to_bottom(browser)

        return articles_set

    def __get_url_from_page(self, page_source) -> List[str]:
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
