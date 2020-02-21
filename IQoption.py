#!/usr/bin/python3
import time
from os import path 
import pprint
from iqoptionapi.stable_api import IQ_Option


def main():
	if path.exists("iqdataset.csv") == False:
		with open("iqdataset.csv", 'w') as esc:
			esc.write("{};{}".format("timestamp","varkandle\n"))
			esc.close()
	else:
		pass
	iq=IQ_Option("@.com","")
	iq.set_max_reconnect(-1)
	if iq.check_connect() == True:
		while True:
			try:			
				goal="EURJPY"
				size=1
				maxdict=10
				iq.start_candles_stream(goal,size,maxdict)
				cc=iq.get_realtime_candles(goal, 1)
				pp = pprint.PrettyPrinter(depth=8)
				inti = cc
				tim = time.time()
				end_time = int(tim) - 0.8
				end_cap = inti[int(end_time)]["min"]
				with open("iqdataset.csv", "a") as file:
					file = file.write("{};{}\n".format(end_time,end_cap))
					print(file)
			except Exception as e:
				print("ERRO:", e)
				continue
	if iq.check_connect() == False:
		iq.connect()
		main()

if __name__ == "__main__":
	main()

