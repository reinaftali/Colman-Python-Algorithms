

import datetime
import random
from allSums import *

def getAllSums(arr):

    ret = set()
    
    def allSums(sum,index):
        if index==len(arr):
            ret.add(sum)
            return
        allSums(sum+arr[index],index+1)
        allSums(sum,index+1)
    
    allSums(0,0)
    return ret



arr =[random.randint(1,10) for x in range(20)]

t0 =  datetime.datetime.now()
result = getAllSums(arr)
t1 =  datetime.datetime.now()
delta = t1-t0


t0 =  datetime.datetime.now()
result2 = allSumsDP(arr)
t1 =  datetime.datetime.now()
delta2 = t1-t0


if result != result2:
    print(f"your solution is incorrect (-50)")
if delta2.microseconds*100 >= delta.microseconds:
    print("your solution is not efficent enough (-50)")


print("done")


