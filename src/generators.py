from typing import Any, Dict, Generator, List


def filter_by_currency(
        transactions: List[Dict[str, Any]], currency_code: str
) -> Generator[Dict[str, Any], None, None]:
    """
    функция принимает список транзакций, выводит генератор с нужным нам кодом валюты

    """

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """
    функция принимает список транзакций, выводит генератор с описанием транзакций

    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    генератор должен принимать начальное и конечное значения для генерации диапазона номеров.

    """
    if start <= 0 or end <= 0:
        yield "Error: invalid card range, numbers should be non-negative or zero"
    elif start > 10 ** 16 - 1 or end > 10 ** 16 - 1:
        yield "Error: invalid card number, number too long"
    elif start > end:
        yield "Error: start must be less than or equal to end"
    else:
        for number in range(start, end + 1):
            card_number = str(number)
            card_number = "0" * (16 - len(card_number)) + card_number
            formatted_number = " ".join([card_number[i: i + 4] for i in range(0, 16, 4)])
            yield formatted_number
