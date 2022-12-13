import time #first we will import time package

def countdown(t): #the with the help of def function 
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\n")
        time.sleep(1)
        t -= 1

    print('Timer completed!')

t = input('Enter the time in seconds: ')

countdown(int(t))