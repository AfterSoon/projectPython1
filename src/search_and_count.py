import re
from collections import Counter
from typing import Any


def searching_operations_by_re_string(
        transactions: list[dict[str, Any]], string_for_search: re.Pattern
) -> list[dict[str, Any]]:
    """Функция для поиска транзакции по re-строке"""
    filtered_operations = []
    for operation in transactions:
        for value in operation.values():
            match = re.search(string_for_search, str(value))
            if match:
                filtered_operations.append(operation)
    if filtered_operations == []:
        print("Совпадений не найдено")
        return []
    else:
        return filtered_operations


def counting_operations(transactions: list[dict[str, [str, int]]], status_list: list[str]) -> dict[str, int]:
    """Функция подсчета транзакций по описанию"""
    operations_status = []
    for transaction in transactions:
        if transaction.get("description") in status_list:
            operations_status.append(transaction["description"])
    return Counter(operations_status)


def filter_by_description(transactions: list[dict[str, [str, int]]]) -> list[dict[str, [str, int]]]:
    """Функция для фильтрации транзакций по описанию"""
    word_for_filter = input('Введите описание для фильтрации транзакций: ').capitalize()
    filtered_operations = []
    for transaction in transactions:
        if transaction.get("description") == word_for_filter:
            filtered_operations.append(transaction)

    return filtered_operations
