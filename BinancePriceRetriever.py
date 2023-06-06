import requests
import json
from CryptoRecord import CryptoRecord

x = requests.get('https://api.binance.com/api/v3/ticker/24hr?symbol=ADAUSDT')
print(x.status_code)

#print(x.text)

# f = json.loads(x.text)
# symbol = f["symbol"]
# prevClosePrice = f["prevClosePrice"]
# openPrice = f["openPrice"]
# highPrice = f["highPrice"]
# lowPrice = f["lowPrice"]
# record = CryptoRecord(symbol, prevClosePrice, openPrice, highPrice, lowPrice)

# f = open("demofile.txt", "a")
# f.write(symbol + "," + prevClosePrice + "," + openPrice + "," + highPrice + "," + lowPrice + "\n")
# f.close()

f = open("demofile.txt", "a")
f.write(x.text + "\n")
f.close()