import requests

def get_usd_to_krw_dict():
    url = "https://api.frankfurter.dev/v1/latest?base=USD&symbols=KRW"
    response = requests.get(url)
    data = response.json()
    return data_dict

