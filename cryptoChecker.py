import requests
import time
from playsound import playsound

def get_crypto_price(symbol):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[symbol]['usd']

def check_price(symbol, threshold, above_sound, below_sound):
    while True:
        try:
            price = get_crypto_price(symbol)
            print(f"The current price of {symbol} is ${price}")
            if price > threshold:
                playsound(above_sound)
            elif price < threshold:
                playsound(below_sound)
            time.sleep(60)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)

# Example Usage:
# Replace 'bitcoin' with the cryptocurrency symbol of your choice
# Replace 'above_threshold.mp3' and 'below_threshold.mp3' with the paths to your sound files
# Replace 'threshold' with the price threshold you want to set
check_price('bitcoin', 60000, 'above_threshold.mp3', 'below_threshold.mp3')
