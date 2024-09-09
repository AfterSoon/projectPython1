import pytest

from src import filter_by_state, get_date, mask_account_card, mask_account_number, mask_card_number, sort_by_date


# Фикстуры для тестирования
@pytest.fixture
def card_numbers():
    return [
        ("1234567812345678", "************5678"),
        ("1234-5678-1234-5678", "************5678"),
        ("12345678", "********"),
        ("", ""),
        ("abcd", ""),
    ]


@pytest.fixture
def account_numbers():
    return [
        ("12345678901234567890", "******************67890"),
        ("12345", "*****"),
        ("", ""),
    ]


@pytest.fixture
def test_date():
    return [
        {"state": "active", "date": "2023-01-01"},
        {"state": "inactive", "date": "2023-01-02"},
        {"state": "active", "date": "2023-01-03"},
    ]


@pytest.fixture
def dates():
    return [
        ("2023-01-01", "2023-01-01"),
        ("01/01/2023", "2023-01-01"),
        ("Invalid Date", None),
    ]


# Тесты для модуля masks
def test_mask_card_number(card_numbers):
    for number, expected in card_numbers:
        assert mask_card_number(number) == expected


def test_mask_account_number(account_numbers):
    for number, expected in account_numbers:
        assert mask_account_number(number) == expected


# Тесты для модуля widget
def test_mask_account_card():
    assert mask_account_card("1234567812345678") == "************5678"
    assert mask_account_card("12345678901234567890") == "******************67890"
    assert mask_account_card("invalid_input") == "invalid_input"


# Тесты для модуля processing
def test_filter_by_state(test_data):
    assert filter_by_state(test_data, "active") == [
        {"state": "active", "date": "2023-01-01"},
        {"state": "active", "date": "2023-01-03"},
    ]
    assert filter_by_state(test_data, "inactive") == [
        {"state": "inactive", "date": "2023-01-02"},
    ]
    assert filter_by_state(test_data, "nonexistent") == []


@pytest.mark.parametrize("data, expected", [
    ({"state": "active", "date": "2023-01-01"}, True),
    ({"state": "inactive", "date": "2023-01-02"}, True),
])
def test_sort_by_date(test_data, data, expected):
    sorted_data = sort_by_date(test_data)
    assert sorted_data[0]["date"] == data["date"] if expected else True


# Тесты для функции get_data
@pytest.mark.parametrize("input_date, expected_output", dates())
def test_get_data(input_date, expected_output):
    assert get_date(input_date) == expected_output
