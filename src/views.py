import datetime

from src.utils import get_excel
from user_settings_json import add_to_list, get_current_stock, settings


def hello(current_time):
    """Функция приветствия, возвращающая соответствующее сообщение в зависимости от времени суток."""
    try:
        current_time = datetime.datetime.strptime(current_time, "%d.%m.%Y %H:%M:%S")
    except ValueError:
        raise ValueError("Некорректный формат времени")
    current_time = current_time.time()
    night_end = datetime.time(2, 59, 59)
    morning_start = datetime.time(5, 0, 0)
    morning_end = datetime.time(11, 59, 59)
    evening_start = datetime.time(17, 0, 0)
    evening_end = datetime.time(23, 59, 59)
    if current_time <= night_end:
        return "Доброй ночи!"
    elif morning_start <= current_time <= morning_end:
        return "Доброе утро!"
    elif evening_start <= current_time <= evening_end:
        return "Добрый вечер!"
    else:
        return "Добрый день!"


current_transactions = []
transaction_for_print = [{}]
cards = []
top_list = []


def generate_json(current_date):
    """Функция, возвращающая отфильтрованные по дате транзакции"""
    for transaction in get_excel("dict"):
        if (
            str(transaction["Дата платежа"])[2:10] == current_date[2:10]
            and str(transaction["Дата платежа"])[:2] <= current_date[:2]
        ):
            current_transactions.append(transaction)
    return current_transactions


def filtered_cards():
    """Функция, возвращающая правильный список карт"""
    for transaction in current_transactions:
        card = {
            "last_digit": transaction["Номер карты"],
            "total_spent": transaction["Сумма операции"],
            "cashback": round(transaction["Сумма операции"] / 100, 2),
        }
        cards.append(card)
    return cards


def filtered_top():
    """Функция, возвращающая топ 5 транзакций по платежам"""
    sort_current_transactions = sorted(
        current_transactions, reverse=True, key=lambda x: abs(x["Сумма платежа"])
    )
    for transaction in sort_current_transactions:
        top = {
            "date": transaction["Дата платежа"],
            "amount": abs(transaction["Сумма платежа"]),
            "category": transaction["Категория"],
            "description": transaction["Описание"],
        }
        top_list.append(top)
        if len(top_list) == 5:
            break
    return top_list


def final_list(current_date):
    generate_json(current_date)
    filtered_cards()
    filtered_top()
    transaction_for_print[0]["greeting"] = hello(current_date)
    transaction_for_print[0]["cards"] = cards
    transaction_for_print[0]["top_transactions"] = top_list
    transaction_for_print[0]["currency_rates"] = add_to_list()
    transaction_for_print[0]["stock_prices"] = get_current_stock(settings)
    return transaction_for_print


# print(final_list("01.11.2021 23:50:17"), sep="\n")
