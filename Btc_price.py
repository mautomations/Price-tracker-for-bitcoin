import requests, time
from datetime import datetime

while True:
    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    price = data["bpi"]["EUR"]["rate"]
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] Bitcoin: {price} EUR")
    time.sleep(10)
