def mask_account_card(info: str) -> str:
    """Функция работы с номером карты и номером счета, сначала разделяем их, далее маскируем в блоке if"""
    # Разделяем строку на тип и номер
    parts = info.split()
    card_type = ' '.join(parts[:-1])  # Все, кроме последнего элемента
    number = parts[-1]  # Последний элемент - это номер

    if card_type.lower() in ['visa', 'mastercard', 'maestro']:
        # Маскировка номера карты: оставляем первые 4 и последние 4 цифры
        masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
        return f"{card_type} {masked_number}"
    elif card_type.lower() == 'счет':
        # Маскировка номера счета: оставляем последние 4 цифры
        masked_number = f"**{number[-4:]}"
        return f"{card_type} {masked_number}"
    else:
        raise ValueError("Неизвестный тип карты или счета.")


def get_date(date_str: str) -> str:
    """Функция принимает строку с полной датой и выдает более упрощенную в виде день-месяц-год"""
    # Разбиваем строку по символу 'T' и берем только первую часть
    date_part = date_str.split('T')[0]
    year, month, day = date_part.split('-')
    # Форматируем дату в нужный формат
    return f"{day}.{month}.{year}"
