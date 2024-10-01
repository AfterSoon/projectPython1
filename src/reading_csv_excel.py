import pandas as pd
import logging

read_csv_excel_logger = logging.getLogger("reading_csv_excel")
file_handler = logging.FileHandler("logs/reading_csv_excel.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
read_csv_excel_logger.addHandler(file_handler)
read_csv_excel_logger.setLevel(logging.INFO)


def reading_transactions(path_to_file: str) -> list[dict]:
    """Функция чтения данных из csv и Excel файлов"""
    read_csv_excel_logger.info('Work started')
    try:
        if '.csv' in path_to_file[-4:]:
            df = pd.read_csv(path_to_file, delimiter=';')
            read_csv_excel_logger.info('Creating a DataFrame from a csv file is successful')
            result = df.to_dict(orient='records')
            read_csv_excel_logger.info('The work is completed')
            return result
        else:
            df = pd.read_excel(path_to_file)
            read_csv_excel_logger.info('Creating a DataFrame from a Excel file is successful')
            result = df.to_dict(orient='records')
            read_csv_excel_logger.info('The work is completed')
        return result
    except FileNotFoundError:
        read_csv_excel_logger.warning('File not found. Incorrect path to file')
        read_csv_excel_logger.info('The work is completed')
        print('Файл не найден')
        return []
