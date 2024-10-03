import re

from config import PATH_TO_CSV, PATH_TO_JSON, PATH_TO_XLSX
from src.widget import get_date
from src.processing import filter_by_state, sort_by_date
from src.reading_csv_excel import reading_transactions
from src.search_and_count import filter_by_description, searching_operations_by_re_string
from src.utils import get_transactions_dictionary, transaction_amount_in_rub, convert_to_rub, reading_json
from src.widget import mask_account_card


def main():
    status_for_filtering_transactions = ["EXECUTED", "CANCELED", "PENDING"]
    print(
        """Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n"""
    )

    while True:
        choose_a_method = input("Выберите подходящий метод: ")
        if choose_a_method == "1":
            print("\nДля обработки выбран JSON-файл.")
            transactions = reading_json(PATH_TO_JSON)
            break
        elif choose_a_method == "2":
            print("\nДля обработки выбран CSV-файл.")
            transactions = reading_transactions(PATH_TO_CSV)
            break
        elif choose_a_method == "3":
            print("\nДля обработки выбран XLSX-файл.")
            transactions = reading_transactions(PATH_TO_XLSX)
            break
        else:
            continue

    while True:
        print(
            """\nВведите статус, по которому необходимо выполнить фильтрацию.\n
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
        )
        status_for_search = input("Введите статус для поиска транзакций: ")
        if status_for_search.upper() in status_for_filtering_transactions:
            filtered_transactions = filter_by_state(transactions, status_for_search)
            break
    while True:
        print("\nОтсортировать операции по дате? Да/Нет")
        sorting_by_date = input()
        if sorting_by_date == "нет":
            sorted_transactions = filtered_transactions
            break
        else:
            print("\nОтсортировать по возрастанию или по убыванию?")
            sorting_up_down = input()
            if sorting_by_date.lower() == "да" and sorting_up_down.lower() == "по возрастанию":
                sorted_transactions = sort_by_date(filtered_transactions, is_sort=False)
                break
            elif sorting_by_date.lower() == "да" and sorting_up_down.lower() == "по убыванию":
                sorted_transactions = sort_by_date(filtered_transactions)
                break
            else:
                continue
    while True:
        print("\nВыводить только рублевые тразакции? Да/Нет")
        answer = input()
        pattern = re.compile(r"\bRUB\b")
        if answer.lower() == "да":
            new_transactions = searching_operations_by_re_string(sorted_transactions, pattern)
            break
        elif answer.lower() == "нет":
            new_transactions = sorted_transactions
            break
        else:
            continue

    while True:
        print("""\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет""")
        filtred_or_no = input()
        if filtred_or_no.lower() == "да":
            print(
                """\n
Доступные для фильтровки описания: Открытие вклада, Перевод организации, Перевод с карты на карту,
Перевод со счета на счет"""
            )
            total_transaction_list = filter_by_description(new_transactions)
            break
        else:
            total_transaction_list = new_transactions
            break
    print(
        f"\nРаспечатываю итоговый список транзакций...\n\n"
        f"Всего банковских операций в выборке: {len(total_transaction_list)}\n"
    )
    if len(total_transaction_list) == 0:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for operation in total_transaction_list:
            date = get_date(operation.get("date"))
            if choose_a_method == "1":
                currency_name = operation["operationAmount"]["currency"]["name"]
                amount = operation["operationAmount"]["amount"]
                if operation.get("description") == "Открытие вклада":
                    result = (
                        f"{date} {operation['description']}\n{mask_account_card(operation.get('to'))}\n"
                        f"Сумма: {amount} {currency_name}"
                    )
                else:
                    result = (
                        f"{date} {operation['description']}\n"
                        f"{mask_account_card(operation.get('from'))} -> {mask_account_card(operation.get('to'))}"
                        f"\nСумма: {amount} {currency_name}"
                    )
            else:
                currency_name = operation["currency_name"]
                amount = operation["amount"]
                if operation.get("description") == "Открытие вклада":
                    result = (
                        f"{date} {operation['description']}\n{mask_account_card(operation.get('to'))}\n"
                        f"Сумма: {amount} {currency_name}"
                    )
                else:
                    result = (
                        f"{date} {operation['description']}\n{mask_account_card(operation.get('from'))} -> "
                        f"{mask_account_card(operation.get('to'))}\nСумма: {amount} {currency_name}"
                    )
            print(result)
            print("\n")


if __name__ == "__main__":
    main()
