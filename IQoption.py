#!/usr/bin/python3

import time
from os import path 
import pprint
from iqoptionapi.stable_api import IQ_Option

def main():
	if not path.exists("iqdataset.csv"):
		with open("iqdataset.csv", 'w') as esc:
			esc.write("timestamp;varkandle\n")
			esc.close()
	else:
		pass
	iq = IQ_Option("","") # Login do user
	iq.set_max_reconnect(-1)
	if iq.check_connect():
		while True:
			time.sleep(15) #Tempo para coletar, e sim, isso causa no resultado influência!
			try:			
				goal     = "EURUSD" # ATIVO 
				size     = 1
				maxdict  = 10
				iq.start_candles_stream(goal, size, maxdict)
				cc       = iq.get_realtime_candles(goal, 1)
				pp       = pprint.PrettyPrinter(depth = 8)
				inti     = cc
				tim      = time.time()
				end_time = int(tim) - 0.8
				end_cap  = inti[int(end_time)]["min"]
				with open("iqdataset.csv", "a") as file:
					file = file.write(f"{end_time};{end_cap}\n")
					print(file)
			except Exception as e:
				print("ERRO:", e)
				continue
	if not iq.check_connect():
		iq.connect()
		main()

if __name__ == "__main__":
	main()


