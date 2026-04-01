import requests
import dotenv
import datetime
import os

dotenv.load_dotenv()

key = os.getenv("EXCHANGE_TOKEN")
base = "USD"
output = "json"

url = f"https://currencyapi.net/api/v2/rates?key={key}&base={base}&output={output}"
headers = {
    'Accept': 'application/json'
}

def get_usd_to_krw_dict():
    response = requests.get(url, headers=headers)
    data = response.json()
    dt_utc = datetime.datetime.utcfromtimestamp(int(data["updated"]))
    dt_kst = dt_utc + datetime.timedelta(hours=9)
    data["date"] = dt_kst
    return data

