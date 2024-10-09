import pytest

import pandas as pd

from src.reading_csv_excel import reading_transactions

from unittest.mock import patch


@pytest.fixture
def test_df() -> pd.DataFrame:
    """Фикстура, создающая тестовый DataFrame"""

    test_dict = {

        "id": [650703.0, 3598919.0],

        "state": ["EXECUTED", "EXECUTED"],

        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],

        "amount": [16210.0, 29740.0],

        "currency_name": ["Sol", "Peso"],

        "currency_code": ["PEN", "COP"],

        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],

        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],

        "description": ["Перевод организации", "Перевод с карты на карту"]

    }

    return pd.DataFrame(test_dict)


@patch('src.reading_csv_excel.pd.read_csv')
def test_reading_transactions(mock_read, test_df):
    # Настраиваем мок так, чтобы он возвращал наш тестовый DataFrame

    mock_read.return_value = test_df

    # Тестируем функцию, сравнивая результат с ожидаемым

    result = reading_transactions('C:/Users/User/PycharmProjects/hometask_ver2/data/transactions.csv')

    expected = test_df.to_dict(orient='records')

    assert result == expected


def test_reading_transaction_with_incorrect_path():
    # Тестируем случай с некорректным путем

    assert reading_transactions("") == []
