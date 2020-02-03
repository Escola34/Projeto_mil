#! /usr/bin/python3
from yahoo_finance_api2 import share
import pprint, time

while True:
    try:
        teste = share.Share("BTC-USD")
        date = None
        date = teste.get_historical(share.PERIOD_TYPE_DAY, 1, share.FREQUENCY_TYPE_MINUTE, 1 )
        pp = pprint.PrettyPrinter(depth=7)
        timestamp = date['timestamp'][-5]
        ope = date['open'][-1]
        high = date['high'][-1]
        low = date['low'][-1]
        close = date['close'][-1]
        volume = date['volume'][-1]

        print("Aberto: %.3f" % ope)
        print("Alta: %.3f" % high)
        print("Baixa: %.3f" % low)
        print("volume: %.3f\n" % volume)
        print("time: %.3f\n" % timestamp)
        time.sleep(60)
    except Exception as e:
        print("ERROR:", e)
