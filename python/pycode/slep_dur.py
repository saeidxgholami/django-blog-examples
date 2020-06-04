sleep = 2230 
wakeup = 630 

if sleep > 1200:
    sleep -= 1200
    print(sleep-wakeup)
else:
    print(wakeup-sleep)
