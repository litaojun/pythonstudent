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
    a = (1,1,2,3,5,8,13,21,34,55,88,143)
    s = lambda x,y:(x,y)+s(x+y,x+y+y) if x+y<100  else (x,y) if y<100 else (x,)
    m = lambda x,y:(x,)+m(y,x+y) if y<100 else (x,)
    print s(1,1)
    print m(1,1)
if __name__ == '__main__':
    a()
    b()
    print (1,)+(2,)+(3,)