#!/usr/bin/env python
# encoding: utf-8
'''
Created on May 21, 2017

@author: Administrator
'''
#is == 区别
import types
def a():
    a = "abc"
    b = "abc"
    c = a 
    d = "abcd"
    e = "abc"
    print a==b ,type(a) is types.StringType,type(a) == type(b)
    #a==b表示a和b指向的值相等
    print a==c 
    print a is b 
    print a is c 
    print a==d 
    print a is d
    print a == e
    print a is e
def b():
    a = [1,2,"abc"]
    b = [2,1,"abc"]
    c = a 
    d = [1,2,"abc"]
    print a == b    #false,对应的值不相等；
    print a == c ,a is c  #a==c true对应值相等；a is c True两个为同一个对象
    print a == d , a is d  #a==d true对应值相等；a is d False两个不为同一个对象
def c():
    a = 1000
    b = 1000
    c =  1.5
    d = 1.5
    print a is b,id(a),id(b)   #a is b相当于id(a) == id(b) 即a和b为同一个对象，比较结果应该为false，但由于python缓存原因导致结果为false
    print c is d,id(c),id(d)   #详见《python核心编程》第63页 
class A(object):
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, obj):
        return self.name == obj.name
def d():
    a = A("Leon")
    b = A("Leon")
    print a == b
    
if __name__ == '__main__':
   d()