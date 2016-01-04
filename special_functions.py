import math
from math import exp

def linear(x,a):
    if x<= -1:
        return math.log(linear(x,a),a)
    if -1 < x and x <=0:
        return 1 + x
    if 0 < x:
        return a**(linear(x-1,a))

def superlog(n):
    if n<=1:
        return 0
    if n > 1:
        return 1 + superlog(math.log(n,2))
print(superlog(17))

def ackermann(m,n):
    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return ackermann(m-1,1)
    if m > 0 and n > 0:
        return ackermann(m-1,ackermann(m,n-1))
def graham():
    pass
def g_log(x):
    if 0 <= x and x < 1:
        return x
    if x >= 1:
        return 1 + g_log(math.log(x,math.e))
        
def sli(x):
    x = g_log(x)
    y = math.floor(x)
    return (y,x-y)
