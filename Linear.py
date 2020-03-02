#!/usr/bin/python3
import pandas as pd
from time import strftime
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import time 
import numpy as np
from iqoptionapi.stable_api import IQ_Option



def buy():
	#Função de compra
	I_want_money=IQ_Option("","")
	Money=10
	ACTIVES="EURUSD"#Ativo para compra
	ACTION="call"
	expirations_mode=1
	id=I_want_money.buy(Money,ACTIVES,ACTION,expirations_mode)
	id2=I_want_money.buy(Money,ACTIVES,ACTION,expirations_mode)


while  True:
	try:
		time.sleep(59)#Resultado para cada 59 segundos. Altere se quiser
		dataframe = pd.DataFrame()
		read = pd.read_csv("iqdataset.csv", delimiter=";")
		dataframe['x'] = read["timestamp"] 
		dataframe['y'] = read["varkandle"] 
		x_values = np.log(dataframe[['x']])
		y_values = np.log(dataframe[['y']])
		model = linear_model.LinearRegression()
		fit= model.fit(x_values, y_values)
		preditx = model.predict(x_values)
		MSE = mean_squared_error(y_values, preditx)
		CED = r2_score(y_values, preditx)
		print("MeSE", MSE)
		tu = strftime("%H:%M:%S")
		print("R2:%.2f" %(CED), "|", tu)
	except  Exception as E:
		print(E)






