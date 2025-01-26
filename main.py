from src.masks import get_mask_card_number, get_mask_account


def main():
    card_number = "7000792289606361"
    masked_card_number = get_mask_card_number(card_number)
    print(f"Маскированный номер карты: {masked_card_number}")

    account_number = "73654108430135874305"
    masked_account_number = get_mask_account(account_number)
    print(f"Маскированный номер счета: {masked_account_number}")

if __name__ == "__main__":
    main()