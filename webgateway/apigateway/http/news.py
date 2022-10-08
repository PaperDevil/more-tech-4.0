from ninja import Router

from apigateway.mongodb import get_post_collection
from apigateway.schemas.responses.news import NewsResponse
from apigateway.schemas.requests.pagination import PageSchema
from apigateway.schemas.requests.categories import CategoriesSchema


news_router = Router()


@news_router.get('/all', response=list[NewsResponse])
def get_hot_news(request, limit: int, offset: int):
    """
    Метод для получения полного списка новостей.

    :param request:
    :param page:
        contains limit & offset
    :param categories:
        contains list of searching categories
    """
    data = get_post_collection()
    result = []
    for item in data.feature_store.posts.find({}).skip(offset).limit(limit):
        result.append(NewsResponse(
            title=item['title'],
            content=item['text']
        ))
    return result


@news_router.get('/digest', response=list[NewsResponse])
def get_digest(request):
    """
    Метод для получения дайджеста за сегодня.

    :param request:
    :return:
    """
    return ...


@news_router.get('/{int:id}', response=NewsResponse)
def get_news_detail(request, id):
    """
    Метод для получения полной информации о новости.

    :param request:
    :param id:
    :return:
    """
    return ...


@news_router.get('/trends')
def get_trends(request, days: int):
    """
    Получение списка трендов за определённый период

    :param request:
    :param days:
        Количество дней для которых нужно просчитать тренды
    :return:
    """
    return ...


@news_router.get('/trend/{str:trend}', response=list[NewsResponse])
def get_trendet_news(request, trend: str):
    """
    Получение списка новостей по какому-то тренду

    :param request:
    :return:
    """
    ...