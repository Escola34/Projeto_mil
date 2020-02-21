#! /usr/bin/python3
from yahoo_finance_api2 import share
import pprint, time
from datetime import  datetime

while True:
    try:
        teste = share.Share("BTC-USD")
        date = None
        date = teste.get_historical(share.PERIOD_TYPE_DAY, 1, share.FREQUENCY_TYPE_MINUTE, 5)
        pp = pprint.PrettyPrinter(depth=7)
        
        ope = date['open'][-1]
        high = date['high'][-1]
        low = date['low'][-1]
        close = date['close'][-1]
        low = "%.2f" %(low)          

        now =datetime.now()
        hora = now.strftime('%d-%m-%y;%H:%M:%S')
        al = str('{};{}'.format(hora, low))
        print(al)
        with open('dataset_Yahoo.csv', 'a') as csvfile:
            file = csvfile.write(al+'\n')

        time.sleep(60)
    except Exception as e:
        print("ERROR:", e)
