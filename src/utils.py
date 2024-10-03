import json
import logging
import os
from typing import Any

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv()
api_key = os.getenv("API_KEY")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    filemode="w",
)

logger = logging.getLogger("utils")


def get_transactions_dictionary(path: str) -> Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info("Getting transaction list starts")
        with open(path, "r", encoding="utf-8") as operations:
            try:
                transactions_data = json.load(operations)
                logger.info("Transactions list ready")
                return transactions_data
            except json.JSONDecodeError:
                logger.error("Decode error")
                transactions_data = []
                return transactions_data
    except FileNotFoundError:
        logger.error("File was not found")
        transactions_data = []
        return transactions_data


def transaction_amount_in_rub(transactions: list, transaction_id: int) -> Any:
    """Принимает транзакцию и возвращает сумму в рублях, если операция не в рублях, конвертирует"""
    logger.info("Getting operation amount starts")
    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                rub_amount = transaction["operationAmount"]["amount"]
                logger.info(f"Operation amount in RUB:{rub_amount}")
                return rub_amount
            else:
                transaction_convert = dict()
                transaction_convert["amount"] = transaction["operationAmount"]["amount"]
                transaction_convert["currency"] = transaction["operationAmount"]["currency"]["code"]
                logger.info(f"Operation amount in {transaction_convert["currency"]}:{transaction_convert["amount"]}")
                #                print(transaction_convert)
                rub_amount = round(convert_to_rub(transaction_convert), 2)
                if rub_amount != 0:
                    logger.info(f"Operation amount in RUB:{rub_amount}")
                    return rub_amount
                else:
                    logger.error("Operation amount can't be converted to RUB")
                    return "Конвертация не может быть выполнена"
    else:
        return "Транзакция не найдена"


def convert_to_rub(transaction_convert: dict) -> Any:
    amount = transaction_convert["amount"]
    currency = transaction_convert["currency"]
    """Принимает значение в долларах или евро, обращается к внешнему API и возвращает конвертацию в рубли"""
    try:
        if currency == "USD":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
            headers = {"apikey": api_key}
            response = requests.get(url, headers=headers)
            json_result = response.json()
            rub_amount = json_result["result"]
            return rub_amount
        elif currency == "EUR":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}"
            headers = {"apikey": api_key}
            response = requests.get(url, headers=headers)
            json_result = response.json()
            rub_amount = json_result["result"]
            logger.info(f"Operation amount in USD/EUR in RUB:{rub_amount}")
            return rub_amount
    except RequestException:
        return 0


# if __name__ == "__main__":
#    transactions = get_transactions_dictionary("../data/operations.json")
#    print(transaction_amount_in_rub(transactions, 41428829))

from json import JSONDecodeError

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    filename="logs/utils.log",
    filemode="w",
)
utils_logger = logging.getLogger("utils")


def reading_json(path_to_file: str) -> list:
    """Функция читает json файл с транзакциями и выдает их список"""
    utils_logger.info("Запуск программы")
    try:
        with open(path_to_file, encoding="UTF-8") as file:
            j_file = json.load(file)
            result = isinstance(j_file, list)
            if result and j_file != []:
                utils_logger.info("Данные успешно получены")
                return j_file
            else:
                utils_logger.warning("Ошибка данных")
                return []
    except FileNotFoundError:
        utils_logger.error("Файл не найден")
        print("Файл не найден")
        return []
    except JSONDecodeError:
        utils_logger.error("Пустой файл")
        print("Некорректные данные")
        return []
