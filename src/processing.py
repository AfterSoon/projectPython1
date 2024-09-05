from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Функция фильтрует список словарей по значению ключа 'state'.
    """
    return [item for item in data if item.get('state') == state]


"""# Пример использования:
data = [
    {'id': 1, 'state': 'EXECUTED', 'amount': 100},
    {'id': 2, 'state': 'PENDING', 'amount': 200},
    {'id': 3, 'state': 'EXECUTED', 'amount': 300}
]

filtered_data = filter_by_state(data)
print(filtered_data)"""

from datetime import datetime


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Функция сортирует список словарей по значению ключа 'date'.
    """
    return sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=descending)


"""# Пример использования:
data = [
    {'id': 1, 'date': '2023-10-01', 'amount': 100},
    {'id': 2, 'date': '2023-09-15', 'amount': 200},
    {'id': 3, 'date': '2023-10-05', 'amount': 300}
]

sorted_data = sort_by_date(data)
print(sorted_data)"""
