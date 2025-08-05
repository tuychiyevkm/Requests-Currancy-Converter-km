def get_user_input():
    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From currency (USD, UZS, EUR): ").upper()
        to_currency = input("To currency (USD, UZS, EUR): ").upper()

        if from_currency not in ("USD", "UZS", "EUR") or to_currency not in ("USD", "UZS", "EUR"):
            raise ValueError("Noto‘g‘ri valyuta turi.")

        return amount, from_currency, to_currency
    except ValueError as ve:
        print( ve)
        return None, None, None

def show_result(amount, from_currency, to_currency, result, date):
    print(f"\n✅ {amount:.2f} {from_currency} = {result:,.2f} {to_currency} ({date})")
