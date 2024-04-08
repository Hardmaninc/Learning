import requests

def convert_currency(amount, from_currency, to_currency):
    base_url = "https://api.exchangerate-api.com/v4/latest/"

    # Fetch latest exchange rates
    response = requests.get(base_url + from_currency)
    data = response.json()

    if 'rates' in data:
        rates = data['rates']
        if from_currency == to_currency:
            return amount

        if from_currency in rates and to_currency in rates:
            conversion_rate = rates[to_currency] / rates[from_currency]
            converted_amount = amount * conversion_rate
            return converted_amount
        else:
            raise ValueError("Invalid currency!")
    else:
        raise ValueError("Unable to fetch exchange rates!")
    
amount = float(input("Amount? \n"))
from_currency = (input("from currency \n")).upper()
to_currency = input("to currency \n").upper()
converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")