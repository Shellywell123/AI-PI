# from features import date_time
# from features import weather
# from features import ip
# from features import stock
import threading
import os

alarm_time = "22:00"
alert = 'Wake Up!'

def thread_loop():
    """
    """
    entry_every_N_mins = 1
    minute = 60
    threading.Timer(entry_every_N_mins*minute, thread_loop).start()

    # check alarm every minute
    from features.alarm import alarm_check
    if alarm_check(alarm_time) == True:
        print('\n AI-PI: "{}"'.format(alert))
        os.system('espeak {}'.format(alert))
        from features import date_time,weather

thread_loop()
