#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2017年5月23日

@author: li.taojun
'''
def a():
    s = lambda x:"yes" if x==1 else "no"
    s(0)
    s(1)
    s(2)
def b():
    a = (1,1,2,3,5,8,13,21,34,55,89,144)
    s = lambda x,y:(x,y)+s(x+y,x+y+y) if x+y<100  else (x,y) if y<100 else (x,)
    m = lambda x,y:(x,)+m(y,x+y) if y<100 else (x,)
    print s(1,1)
    print m(1,1)
def c(i=1):
    f = lambda x:f(x-2)+f(x-1) if x>1 else 1
    #return f(i)
    rt = map(f,range(i))
    #g = lambda x:g(x-1)+
    t = zip(range(10),range(10),range(10))
    print t
    for i,num in enumerate((1,1,2,3,5)):
        print i,num
    print t
    
    return rt
if __name__ == '__main__':
    a()
    b()
    print (1,)+(2,)+(3,)
    print c(11)