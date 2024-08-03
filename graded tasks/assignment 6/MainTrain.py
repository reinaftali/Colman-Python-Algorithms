import numpy as np
import matplotlib.pyplot as plt
import random
from convex_hull import *

class Point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y


# simple test case...
X=[0,3,2,3,1,1,2]
Y=[0,3,4,4,5,3,5]
N=len(X)

points=[Point(X[i],Y[i]) for i in range(N)]

p0=findBottomLeft(points)

if p0.x!=0 or p0.y!=0:
    print("you didn't find the left most bottom point (-11)")

sortCCW(points)
sx=[0,3,3,2,2,1,1]
sy=[0,3,4,4,5,3,5]
for i in range(len(points)):
    if points[i].x!=sx[i] or points[i].y!=sy[i]:
        print("wrong order in sortCCW (-2)")


def getPoint(p,R,angle):
    angle = math.radians(angle)
    return Point(p.x+R*math.cos(angle),p.y+R*math.sin(angle))

p0=Point(0,0)
R=100
for i in range(0,360,36):
    mid=getPoint(p0,R,i)
    left=getPoint(p0,R,(i+10)%360)
    right=getPoint(p0,R,(i-10)%360)
    if not isLeftTurn(p0,mid,left):
        print("problem detecting a left turn (-1)")
    if isLeftTurn(p0,mid,right):
        print("problem not detecting a left turn (-1)")


S = grahamScan(points)
ax=[0,3,3,2,1,0]
ay=[0,3,4,5,5,0]

if len(S)!=len(ax):
    print("your solution for the simple case is wrong (-5)")
else:
    ok =True
    for i in range(len(S)):
        if S[i].x!=ax[i] or S[i].y!=ay[i]:
            ok=False
    if not ok:
        print("your solution for the simple case is wrong (-5)")

# general case

N=50
X=[random.randint(-100,100) for i in range(N)]
Y=[random.randint(-100,100) for i in range(N)]
points=[Point(X[i],Y[i]) for i in range(N)]

S = grahamScan(points)

def tst(p):
    def chk(p1, p2, p3):
        return (p2.y - p1.y) * (p3.x - p2.x)-(p2.x - p1.x) * (p3.y - p2.y)>0
    for i in range(1,len(S)):
        if chk(S[i-1],S[i],p):
            return False
    return True

for p in points:
    if p not in S and not tst(p):
        print("a point is outside the convex hull (-1)")

print("done")

# use for visual debug
xs=[S[i].x for i in range(len(S))]
ys=[S[i].y for i in range(len(S))]
plt.plot(xs,ys,'')
plt.scatter(np.array(X),np.array(Y))
plt.show()





