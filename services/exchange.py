import requests

API_URL = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

def get_exchange_rates():
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()

    rates = {}
    for item in data:
        if item["Ccy"] in ("USD", "EUR"):
            rates[item["Ccy"]] = {
                "rate": float(item["Rate"].replace(",", "")),
                "date": item["Date"]
            }
    return rates
