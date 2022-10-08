from abc import ABC, abstractmethod
from typing import List

from Article import Article


class ArticleDataSource(ABC):
    """Источник данных статей. Парсеры, классы работы с API должны унаследовать этот класс"""

    @abstractmethod
    def get_data(self) -> List[Article]:
        pass
