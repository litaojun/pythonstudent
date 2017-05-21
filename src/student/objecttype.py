#!/usr/bin/env python
# encoding: utf-8
'''
Created on May 21, 2017

@author: Administrator
'''
class acls:
    def __init__(self):
        self.a = 1  
    def __str__(self):
        return str(self.a)
def afunc():
    a = 9
    print id(a)   #输出a的身份
    print type(a) #输出a的类型
    print a       #输出a的值ֵ
def bfunc():
    a = acls()
    print id(a)
    print type(a)
    print a
if __name__ == "__main__":
    afunc()
    bfunc()