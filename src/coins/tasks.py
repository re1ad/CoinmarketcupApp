from asgiref.sync import async_to_sync
from django.forms.models import model_to_dict
from celery import shared_task
from channels.layers import get_channel_layer

import requests

from .models import Coin


channel_layer = get_channel_layer()


def get_coins_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=h1'
    return requests.get(url).json()


@shared_task
def write_coins():
    data = get_coins_data()
    coins = []
    for coin in data:
        obj, _ = Coin.objects.get_or_create(symbol=coin['symbol'])
        obj.name = coin['name']
        obj.symbol = coin['symbol']

        if obj.price > coin['current_price']:
            state = 'fall'
        elif obj.price < coin['current_price']:
            state = 'raise'
        else:
            state = 'some'

        obj.price = coin['current_price']
        obj.rank = coin['market_cap_rank']
        obj.image = coin['image']
        obj.save()

        new_data = model_to_dict(obj)
        new_data.update({'state': state})
        coins.append(new_data)

    async_to_sync(channel_layer.group_send)('coins', {'type': 'send_new_data', 'text': coins})
