#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2017年5月22日

@author: li.taojun
'''

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __eq__(self,o):
        return self.name == o.name
    def __cmp__(self, other):
        return cmp(self.name, other.name)

if __name__ == "__main__":
    a = MyClass('leon')
    b = MyClass('leon')
    c = MyClass('leona')
    print a is b
    print a == b
    print id(a)
    print id(b)
    print cmp(a, b)
    print a is c
    print a == c
    print id(a)
    print id(c)
    print cmp(a, c)