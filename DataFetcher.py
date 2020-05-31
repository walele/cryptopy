import binanceClient
import sys
from DataManager import DataManager

class DataFetcher   :

    dataMan = 0

    def init(self):
        print('Data Fetcher init...')
        self.dataMan = DataManager()
        self.dataMan.init()

    def fetch(self):
        markets = binanceClient.getBtcMarket()
        print('Number of BTC Markets : ' + str(len(markets)))

        # Init Tables
        for m in markets:
            self.dataMan.initMarket(m)
            sys.stdout.flush()

        # Fetch prices
        for m in markets:
            price = binanceClient.getPrice(m)
            print("Price for %s : %s" %(m, price))
            self.dataMan.insertMartketData(m, price)
            sys.stdout.flush()
