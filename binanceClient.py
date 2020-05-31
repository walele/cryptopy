import requests
baseUrl = 'https://api.binance.com'

def getBtcMarket():
    url = baseUrl + '/api/v3/exchangeInfo'

    r = requests.get(url)
    data = r.json()
    markets = []

    for s in data['symbols']:
        if s['quoteAsset'] == 'BTC':
            markets.append(s['symbol'])

    return markets

def getPrice(market):
    url = baseUrl + '/api/v3/avgPrice?symbol=' + market

    r = requests.get(url)
    data = r.json()

    return data['price']
