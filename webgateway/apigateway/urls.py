from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from apigateway.http import news_router


api = NinjaAPI()
api.add_router('/news/', news_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
