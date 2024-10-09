from src.views import get_excel


def find_numbers(num):
    current_transactions = []
    for transaction in get_excel("dict"):
        if num in transaction["Описание"]:
            current_transactions.append(transaction)
    return current_transactions


# print(*find_numbers('966'), sep='\n')
