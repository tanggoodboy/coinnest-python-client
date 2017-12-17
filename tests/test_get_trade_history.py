# -*- coding: utf-8 -*-
import pytest
from unittest.mock import MagicMock

from coinnest import Coinnest


def test_get_ticker():
    mocked_resposne = [
        {
            "date":"132412341",
            "price":1000,
            "amount":2,
            "tid":"1",
            "type":"buy",
        },
    ]
    coinnest = Coinnest()
    coinnest.get_trade_history = MagicMock(
        return_value=mocked_resposne,
    )
    response = coinnest.get_trade_history(coin='qtum', since=0)
    assert response == mocked_resposne
