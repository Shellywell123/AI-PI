lofi = "https://www.youtube.com/watch?v=5qap5aO4i9A&ab_channel=LofiGirl"

#import pafy
#import vlc

#video = pafy.new(lofi)
#best = video.getbest()
#playurl = best.lofi

#playurl.play()

EXPORT DISPLAY=0:0

import os
os.system('chromium-browser '+lofi)
