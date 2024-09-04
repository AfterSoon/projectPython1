def mask_card_number(card_number: int) -> str:
    """Маскирует номер карты по правилу XXXX XX** **** XXXX."""

    card_str = str(card_number)
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")

    return f"{card_str[0:4]} {card_str[4:6]}** **** {card_str[12:]}"


def mask_account_number(account_number: int) -> str:
    """Маскирует номер счета по правилу **XXXX."""
    account_str = str(account_number)
    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать как минимум 4 цифры.")

    return f"**{account_str[-4:]}"
