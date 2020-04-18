import os 

day   = str(os.popen("date +%A").readlines())[2:-4]
month_int = int(str(os.popen("date +%m").readlines())[2:-4])
date  = str(os.popen("date +%W").readlines())[2:-4]
year  = str(os.popen("date +%Y").readlines())[2:-4]
time  = str(os.popen("date +%X").readlines())[2:-7]


months = ['January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December']

month = months [month_int-1]


info = 'espeak " it is {}, on {} the {} of {}"'.format(time,day,date,month,year)

#print info
os.system(info)