import requests
from pprint import pprint
import webbrowser
import sys

arguments = sys.argv

print(arguments)

symbol = sys.argv[1]
#symbol = input('What Crypto Ticker? ')

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
    name = data.get('data').get(f'{str.upper(symbol)}').get('name')
    print(name)
    print(f'${price:,.2f}')

    open = sys.argv[2]
    if(open == 'y'):
      webbrowser.open(f'https://coinmarketcap.com/currencies/{name.replace(" ", "-")}')
except:
    print("Unable to get price")