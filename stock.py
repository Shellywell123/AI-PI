
import os
import subprocess

ticker = input("Input the ticker of the stock you want to know the price of:\n")

def get_stock_info(ticker):
        """
        """
        try:
                os_str ="curl https://terminal-stocks.herokuapp.com/{}".format(str(ticker))
                os.system(os_str)
                output = subprocess.getoutput(os_str)
                info = list(output.split('\x1b[90m│'))[8:14]

                for n in range(0,len(info)):
                    info[n]= str(info[n]).split('\x1b[39m ')[1]

                name = info[0]
                price = info[1]
                change = info[2]
                per_change = info[3]
                day_range = info[4]
                week_52_range=info[5]


                if per_change[0] == '-':
                    direction = 'down'
                else:
                    direction = 'up'

                ret_str='{} is currently {} {}% trading at {} U.S, dollars'.format(name,direction,per_change,price)
                print(ret_str)
                return ret_str
                
        except:
                print("'{}' is not a vaild ticker, try again".format(ticker))

text = get_stock_info(ticker)
os.system(text)


