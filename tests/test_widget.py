import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            """Maestro 1596837868705199
            Счет 64686473678894779589
            MasterCard 7158300734726758
            Счет 35383033474447895560
            Visa Classic 6831982476737658
            Visa Platinum 8990922113665229
            Visa Gold 5999414228426353
            Счет 736541084301358743""",
            """Maestro 1596 83** **** 5199
            Счет **9589
            MasterCard 7158 30** **** 6758
            Счет **5560
            Visa Classic 6831 98** **** 7658
            Visa Platinum 8990 92** **** 5229
            Visa Gold 5999 41** **** 6353
            Счет Error"""
        ),
    ],
)
def test_mask_account_card(data: str, expected: str) -> None:
    masked_account_card = mask_account_card(data)
    assert masked_account_card == expected

@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-12", "12.12.2023"),
        ("2020-11-10", "10.11.2020"),
    ],
)
def test_get_date(date_str: str, expected: str) -> None:
    date = get_date(date_str)
    assert date == expected