def alarm_check():
    """
    """
    import os 

    day   = str(os.popen("date +%A").readlines())[2:-4]
    month_int = int(str(os.popen("date +%m").readlines())[2:-4])
    date  = str(os.popen("date +%W").readlines())[2:-4]
    year  = str(os.popen("date +%Y").readlines())[2:-4]
    time  = str(os.popen("date +%X").readlines())[2:-7]

    alarm_time = '17:50'

    print ('\n - AI-PI: "'+time)

    if time==alarm_time:
    	os.system('espeak "wake up!"')
