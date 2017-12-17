# -*- coding: utf-8 -*-
import pytest
from unittest.mock import MagicMock

from coinnest import Coinnest


def test_get_ticker():
    mocked_resposne = {
        "high": 12000,
        "low": 10000,
        "buy": 11500,
        "sell": 11800,
        "last": 11800,
        "vol": 15425,
        "time": 1504513064,
    }
    coinnest = Coinnest()
    coinnest.get_ticker = MagicMock(
        return_value=mocked_resposne,
    )
    response = coinnest.get_ticker(coin='qtum')
    assert response == mocked_resposne
