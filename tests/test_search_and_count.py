import re
from collections import Counter

import pytest

from src.search_and_count import counting_operations, searching_operations_by_re_string


def test_searching_operations_by_string(list_with_data: list[dict[str, [str, int]]]):
    """Тест функции поиска транзакций по re-строке"""
    pattern = re.compile(r"\bC\D{6}D\b")
    assert searching_operations_by_re_string(list_with_data, pattern) == [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }
    ]


def test_searching_operations_by_string_var2(list_with_incorrect_date: list[dict[str, [str, int]]]):
    """Тест функции поиска транзакций по re-строке"""
    pattern = re.compile(r"\bE\D{6}D\b")
    assert searching_operations_by_re_string(list_with_incorrect_date, pattern) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.5123"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.42557245"},
    ]


def test_counting_operations(list_with_data: list[dict[str, [str, int]]]):
    """Тест функции на подсчёт операций по описанию"""
    assert counting_operations(list_with_data, ["Перевод организации"]) == Counter({"Перевод организации": 2})


def test_counting_operations_var2(list_with_data: list[dict[str, [str, int]]]):
    """Тест функции на подсчёт операций по описанию"""
    assert counting_operations(list_with_data, ["Перевод организации", "Перевод со счета на счет"]) == Counter(
        ({"Перевод организации": 2, "Перевод со счета на счет": 1})
    )


def test_counting_operations_without_status(list_with_data: list[dict[str, [str, int]]]):
    """Тест функции на подсчёт операций по описанию"""
    assert counting_operations(list_with_data, []) == Counter()
