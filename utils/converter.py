def convert(amount, from_currency, to_currency, rates):
    if from_currency == to_currency:
        return amount

    if from_currency == "UZS":
        return amount / rates[to_currency]["rate"]
    elif to_currency == "UZS":
        return amount * rates[from_currency]["rate"]
    else:
        uzs = amount * rates[from_currency]["rate"]
        return uzs / rates[to_currency]["rate"]
