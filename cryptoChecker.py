import requests
import time
from playsound import playsound

def get_crypto_price(symbol):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[symbol]['usd']

def check_price(symbol, upper_threshold,lower_threshold, above_sound=r"beep-beep-beep-beep-80262.mp3", below_sound=r"beep-beep-beep-beep-80262.mp3"):
    while True:
        try:
            price = get_crypto_price(symbol)
            print(f"The current price of {symbol} is ${price}")
            if price > upper_threshold:
                print("Time to Sell")
                playsound(above_sound)
            elif price < lower_threshold:
                print("Time to Buy")
                playsound(below_sound)
            time.sleep(60)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    check_price('bitcoin', 60000, 'above_threshold.mp3', 'below_threshold.mp3')
