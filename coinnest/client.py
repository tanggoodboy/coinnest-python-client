# -*- coding: utf-8 -*-
import requests

__all__ = ['COINNEST_API_URL', 'Coinnest']

COINNEST_API_URL = 'https://api.coinnest.co.kr'


class Coinnest(object):
    def __init__(self, api_url=COINNEST_API_URL):
        self.api_url = api_url

    class ResponseError(Exception):
        def __init__(self, code=None, description=None):
            self.code = code
            self.description = description

    def get_ticker(self, coin='btc'):
        url = '{}{}?coin={}'.format(self.api_url, '/api/pub/ticker', coin)
        response = requests.get(url)
        return response

    def get_trade_history(self, coin='btc', since=0):
        url = '{}{}?coin={}&since={}'.format(self.api_url, '/api/pub/trades', coin, since)
        response = requests.get(url)
        return response

    def get_depth(self, coin='btc'):
        url = '{}{}?coin={}'.format(self.api_url, '/api/pub/depth', coin)
        response = requests.get(url)
        return response

