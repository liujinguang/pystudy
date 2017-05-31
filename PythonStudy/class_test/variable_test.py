#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月29日

@author: bob
'''

class Person(object):
    name = "aaaa"
    
class Animal(object):
    name = []

if __name__ == '__main__':
    p1 = Person()
    p2 = Person()
    p1.name = "BBB"
    print p1.name
    print p2.name
    
    a1 = Animal()
    a2 = Animal()
    a1.name.append("hello")
    a2.name.append("world")
    
    print a1.name
    print a2.name
    