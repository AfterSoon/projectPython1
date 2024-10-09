import functools
from datetime import datetime
from typing import Optional

import pandas as pd
from dateutil.relativedelta import relativedelta

from src.utils import get_excel


def report_decorator(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "a") as f:
                f.write(f"{result}\n")
            return result

        return wrapper

    return decorator


def date_three_months_ago(date):
    date_format = "%d.%m.%Y"
    date = datetime.strptime(date, date_format)
    new_date = date - relativedelta(months=3)
    return new_date.strftime(date_format)


def date_now():
    now = datetime.now()
    formatted_date = now.strftime("%d.%m.2021")
    return formatted_date


@report_decorator("report.txt")
def spending_by_category(
    transactions: pd.DataFrame, category: str, date: Optional[str] = date_now()
):
    if date is None:
        return []

    date_format = "%d.%m.%Y"
    end_date = datetime.strptime(date, date_format)
    start_date = end_date - relativedelta(months=3)

    current_transactions = []
    for index, transaction in transactions.iterrows():
        if not isinstance(transaction["Дата платежа"], str):
            continue
        transaction_date = datetime.strptime(transaction["Дата платежа"], date_format)
        if (
            transaction["Категория"] == category
            and start_date <= transaction_date <= end_date
        ):
            current_transactions.append(transaction.to_dict())

    return current_transactions


# print(*spending_by_category(get_excel('dataframe'), "Фастфуд", '17.01.2018'), sep='\n')
