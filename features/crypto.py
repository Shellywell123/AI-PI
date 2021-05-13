
import os
import requests

ticker = input("Input the ticker of the crypto you want to know the price of:\n")


def get_live_binance_spot_price(ticker):
    """
    returns live ticker price from binance api in form of a dictionary
    with keys [symbol,price]
    """
    
    try:
        bin_api_url = "https://api.binance.com/api/v1/ticker/price?symbol={}".format(ticker)

        response = requests.get(bin_api_url).json()

        symbol = response['symbol']
        price  = response['price']

        ret_str='{} is currently trading at {} '.format(symbol,price)
        print('\n - AI-PI: "',ret_str,'"')
        return ret_str

    except:
            print("'{}' is not a vaild ticker, try again".format(ticker))


text = get_live_binance_spot_price(ticker)
os.system('espeak "{}"'.format(text))
