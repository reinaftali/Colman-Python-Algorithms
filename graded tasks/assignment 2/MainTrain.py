import threading
from time import sleep
from stream import *

sm = 0
def f(x):
    global sm
    sm+=x

def test1():
    global sm
    c = threading.active_count()
    s = Stream()
    if threading.active_count() != c+1:
        print('you did not open a thread for a stream (-10)')
    
    sm = 0


    s.forEach(f)

    
    for i in range(100):
        s.add(i)        
    
    sleep(1)
    if sm!= 4950:
        print('your forEach method did not work (-10)')
    
    s.stop()

    sleep(0.5)

    if threading.active_count() != c:
        print('you did not close all threads (-10)')


def test2():
    global sm
    c = threading.active_count()
    s = Stream()
    
    sm = 0

    s.apply(lambda x: x%2==0).apply(lambda x : x*10).forEach(f)

    if threading.active_count() != c+3:
        print('you did not open the right ammount of threads (-20)')

    
    for i in range(100):
        s.add(i)        
    
    sleep(1)
    
    if sm!= 24500:
        print('your precessing did not work (-25)')

    s.stop()

    sleep(0.5)

    if threading.active_count() != c:
        print('you did not close all threads (-25)')


# main
test1()
test2()

print("done")