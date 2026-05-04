import requests

def get_crypto_price(coin:str, fiat: str):
    try:    
        response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={fiat}")
        data = response.json()
        if data:
            return data
        else:
            return "No data availible."
    except requests.exceptions.RequestException:
        return f"No data availible."