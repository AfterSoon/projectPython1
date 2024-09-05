from typing import Any, Dict, List
from datetime import datetime


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


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    def parse_date(item):
        return datetime.fromisoformat(item['date'])

    # Сортировка списка по дате
    return sorted(data, key=parse_date, reverse=descending)


""""# Пример входных данных
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]

# Пример использования функции
sorted_data = sort_by_date(data)
print(sorted_data)"""
