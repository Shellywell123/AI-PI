import os

w = str(os.popen("curl wttr.in?format=v2 | grep 'eather'").readlines()).split('\\')

loc  = w[6][25:-18]
temp = w[-7][4:-5]
cond = w[-7][-3:]

text = 'espeak "the current weather in {}, is {} and {} degree celcius"'.format(loc,temp,cond)
print text
os.system(text)