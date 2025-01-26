def get_mask_card_number(card_number: str) -> str:
    """Маска номера банковской карты."""
    return f"{card_number[:6]} {'*' * 6} {card_number[-4:]}"

def get_mask_account(account_number: str) -> str:
    """Маска номера банковского счета."""
    return f"**{account_number[-4:]}"