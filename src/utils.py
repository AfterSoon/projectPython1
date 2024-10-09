import numpy
import pandas as pd


def get_excel(formatting):
    current_transactions = []
    get_excel_file = pd.read_excel("../data/operations.xlsx")
    if formatting == "dataframe":
        return get_excel_file
    elif formatting == "dict":
        for transaction in get_excel_file.to_dict(orient="records"):
            transaction = {
                key: (
                    None if isinstance(value, float) and numpy.isnan(value) else value
                )
                for key, value in transaction.items()
            }
            current_transactions.append(transaction)
        return current_transactions
    else:
        raise ValueError("Invalid format specified. Use 'dataframe' or 'dict'.")


# print(get_excel('dict'))
