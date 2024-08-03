import datetime
import random
import sys
from dnc import *


def minRange(arr,left,right):
    mn=arr[left]
    for i in range(left+1,right+1):
        if mn>arr[i]:
            mn=arr[i]
    return mn

def naiveMaxHistArea(hist):
    maxArea=0
    for i in range(len(hist)):
        for j in range(i,len(hist)):
            area = minRange(hist,i,j) * (j+1-i)
            if maxArea<area:
                maxArea = area
    return maxArea


def run(arr:list,f):
    t0 =  datetime.datetime.now()
    result = f(arr)
    t1 =  datetime.datetime.now()
    delta = t1-t0
    return result , delta.microseconds


mx = dnc(lambda x:x, lambda x,y : max(x,y))
mn = dnc(lambda x:x, lambda x,y : min(x,y))

arr = [random.randint(-10, 10) for i in range(1024)]
if mx(arr) != max(arr):
    print("you got a wrong result for max (-25)")
if mn(arr) != min(arr):
    print("you got a wrong result for min (-25)")


arr = [random.randint(20, 100) for i in range(512)]
nr,nt = run(arr, naiveMaxHistArea)
mr,mt = run(arr, maxAreaHist)


if mr!=nr:
    print("you didn't get the correct result (-25)")
if nt /100 < mt:    
    print("you didn't implement an efficient algo (-25)")


print("done")


