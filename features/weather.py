import os

w = str(os.popen("curl wttr.in?format=v2 | grep 'eather'").readlines()).split('\\')

loc  = (w[0].split(': ')[1]).split(',')[0]
temp = (w[3].split('x1b[0m '))[1][1:].split(',')[0]
cond = w[3].split(',')[1]

text = 'espeak "the current weather in {}, is {} and {} degree celcius"'.format(loc,temp,cond)
print ('\n - AI-PI: "',text.split('"')[1],'"')
os.system(text)
