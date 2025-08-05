from services.exchange import get_exchange_rates
from utils.converter import convert
from interface.cli import get_user_input, show_result

def main():
    try:
        rates = get_exchange_rates()
    except Exception as e:
        print(" Kurslarni olishda xatolik:", e)
        return

    amount, from_currency, to_currency = get_user_input()
    if amount is None:
        return

    try:
        result = convert(amount, from_currency, to_currency, rates)
        date = rates["USD"]["date"]
        show_result(amount, from_currency, to_currency, result, date)
    except Exception as e:
        print(" Hisoblashda xatolik:", e)

if __name__ == "__main__":
    main()
