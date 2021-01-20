from django.urls import path

from .consumers import CoinsConsumer


ws_urlpatterns = [
    path('ws/coins/', CoinsConsumer.as_asgi())
]
