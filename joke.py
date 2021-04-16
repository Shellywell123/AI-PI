import os
import subprocess
import time

output=(subprocess.getoutput("curl https://official-joke-api.appspot.com/random_joke"))

setup = ((output.split('setup":')[1]).split('","punchline"')[0])[1:]
punchline = ((output.split('"punchline":')[1]))[1:-2]

print('\n AI-PI: "',setup,'"')
os.system('espeak "{}"'.format(setup))
time.sleep(5)

print('\n AI-PI: "',punchline,'"')
os.system('espeak "{}"'.format(punchline))
