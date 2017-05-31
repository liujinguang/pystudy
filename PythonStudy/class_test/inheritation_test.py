#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月31日

@author: bob
'''

class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

if __name__ == '__main__':
    print Parent.x, Child1.x, Child2.x
    Child1.x = 2
    print Parent.x, Child1.x, Child2.x
    Parent.x = 3
    print Parent.x, Child1.x, Child2.x
    print dir(Parent)
    print dir(Child1)