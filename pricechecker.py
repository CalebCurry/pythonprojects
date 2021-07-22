import requests
from pprint import pprint

symbol = input('What Crypto Ticker? ')

#url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?CMC_PRO_API_KEY=29cb6142-265e-4850-acf0-6f7c05803c3f&symbol={symbol}'

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '29cb6142-265e-4850-acf0-6f7c05803c3f'
}

parameters = {
    'symbol': symbol
}

response = requests.get(url, headers=headers, params=parameters)

#pprint(response.json())

data = response.json()

try: 
    price = data.get('data').get(f'{str.upper(symbol)}').get('quote').get('USD').get('price')

    print(f'${price:,.2f}')
except:
    print("Unable to get price")