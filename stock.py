import os
import subprocess

ticker = input("Input the ticker of the stock you want to know the price of:\n")

def get_stock_info(ticker):
	"""
	"""
	try:
		os_str ="curl https://terminal-stocks.herokuapp.com/{}".format(str(ticker))
		os.system(os_str)
		cont = subprocess.Popen(os_str, shell=True, stdout=subprocess.PIPE, )
		print('ticker found')
		print(cont.split('|'))
	except:
		print("'{}' is not a vaild ticker, try again")

get_stock_info(ticker)
