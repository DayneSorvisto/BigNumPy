
from functools import reduce
 
 

def arrow(a,b):
    if b == 1:
        return str(a)
    while b > 1:
         return '{}^'.format(str(a)) + "({})".format(arrow(a,b-1))

def power(a,b):
    return b**a
       
def double(a,b):
    list = []
    for i in range(b):
        list.append(a)
    return reduce(power,list)
   
def triple(a,b):
    list = []
    for i in range(b):
        list.append(a)
    return reduce(double,list)
 
def hyper(a,b,func):
    list = []
    for i in range(b):
        list.append(a)
    return reduce(func,list)
 
#now we must construct a list hierarchy containing the first 10 hyperoperators as functions
 
hierarchy = [power,double,triple]
for i in range(2,10):
    hierarchy.append(lambda x,y : hyper(x,y,hierarchy[i]))
print(list)
 
def hyper_n(a,b,n):
    list = []
    for i in range(b):
        list.append(a)
    return reduce(hierarchy[n],list)
 
 
 

    
