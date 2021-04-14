import os

ip = str(os.popen('ifconfig | grep "broadcast"').readlines()).split(' ')[9]
#print ip

text = 'espeak "currently running on {}"'.format(ip)
print(text)
os.system(text)
