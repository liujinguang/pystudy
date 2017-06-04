#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月1日

@author: bob
'''

def singleton(cls, *args, **kwargs):
    instance = {}
    
    def getInstance():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
            
        return instance[cls]
    
    return getInstance

@singleton
class MyClass(object):
    a = 1
    
    def __init__(self, *args, **kwargs):
        pass

if __name__ == '__main__':
    m1 = MyClass()
    m2 = MyClass()
    
    print m1 is m2