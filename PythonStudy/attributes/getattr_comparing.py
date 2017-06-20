#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月20日

@author: bob
'''

class GetAttr(object):
    attr1 = 1
    
    def __init__(self):
        self.attr2 = 2
        
    def __getattr__(self, attr):
        print("GET:" + attr)
        return 3

class GetAttribute(object):
    attr1 = 1
    
    def __init__(self):
        self.attr2 = 2
        
    def __getattribute__(self, attr):
        print("get: " + attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)

if __name__ == '__main__':
    X = GetAttr()
    print(X.attr1)
    print(X.attr2)
    print(X.attr3)
    print('-'*40)
    X = GetAttribute()
    print(X.attr1)
    print(X.attr2)
    print(X.attr3)