# from features import date_time
# from features import weather
# from features import ip
# from features import stock

def thread_loop():
    """
    """
    entry_every_N_mins = 1
    minute = 60
    threading.Timer(entry_every_N_mins*minute, thread_loop).start()

    # check alarm every minute
    from features.alarm import alarm_checker
    alarm_checker()

thread_loop()