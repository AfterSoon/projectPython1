from typing import Any


def filter_by_state(initial_list: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:
    """Принимает на вход список словарей и возвращает новый список,
    содержащий только те словари, у которых ключ state содержит переданное
    в функцию значение."""
    result_list = []
    for num_list in initial_list:
        if num_list.get('state') == state:
            result_list.append(num_list)
    return result_list


def sort_by_date(initial_list: list[dict[str, Any]], reverse_list: bool = True) -> list[dict[str, Any]]:
    """Принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты."""
    sorted_list = sorted(initial_list, key=lambda d: d['date'], reverse=reverse_list)
    return (sorted_list)

#print(filter_by_state(initial_list))
#print(sort_by_date(initial_list))