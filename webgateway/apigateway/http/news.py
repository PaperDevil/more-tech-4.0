from ninja import Router


news_router = Router()

@news_router.get('/hot')
def get_hot_news(request):
    return "..."

