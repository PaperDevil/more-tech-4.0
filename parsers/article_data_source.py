from abc import ABC, abstractmethod
from typing import List

from parsers.article import Article


class ArticleDataSource(ABC):
    """Источник данных статей. Парсеры, классы работы с API должны унаследовать этот класс"""

    @abstractmethod
    def start_parsing(self):
        pass
