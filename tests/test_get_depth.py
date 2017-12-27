from unittest.mock import MagicMock

from coinnest import Coinnest


def test_get_depth():
    mocked_response = {
        "result": True,
        "asks": [
            [5300000, 0.0318],
            [5120000, 0.0199]
        ],
        "bids": [
            [4879000, 1.5],
            [4878000, 0.9643]
        ]
    }
    coinnest = Coinnest()
    coinnest.get_depth = MagicMock(
        return_value=mocked_response,
    )
    response = coinnest.get_depth(coin='btc')
    assert response == mocked_response
