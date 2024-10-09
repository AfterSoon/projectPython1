from unittest.mock import patch

from src.views import final_list, generate_json
from user_settings_json import get_current_price, get_current_stock, settings


def test_generate_json(generate_all_transactions):
    assert generate_json("01.11.2021 23:50:17") == generate_all_transactions
    assert final_list("04.11.2021 23:50:17")[0]["greeting"] == "Добрый вечер!"


def test_top_transactions(top_transactions):
    assert final_list("01.11.2021 23:50:17")[0]["top_transactions"] == top_transactions


@patch("user_settings_json.requests.get")
def test_get_current_price(mock):
    mock.return_value.json.return_value = {"result": get_current_price("USD")}
    result = get_current_price("USD")
    assert result == {"currency": "USD", "rate": 95.61}


@patch("user_settings_json.requests.get")
def test_get_current_stock(mock):
    mock.return_value.json.return_value = {
        "result": [
            {"stock": "AAPL", "price": 226.8},
            {"stock": "MSFT", "price": 416.06},
            {"stock": "GOOGL", "price": 167.06},
            {"stock": "AMZN", "price": 186.51},
            {"stock": "TSLA", "price": 250.08},
        ]
    }
    result = get_current_stock(settings)
    assert result == [
        {"stock": "AAPL", "price": 226.8},
        {"stock": "MSFT", "price": 416.06},
        {"stock": "GOOGL", "price": 167.06},
        {"stock": "AMZN", "price": 186.51},
        {"stock": "TSLA", "price": 250.08},
    ]
