#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 19, 2017

@author: bob
'''
import manynames

if __name__ == '__main__':
    X = 66
    print(X) # 66: the global here
    print(manynames.X) # 11: globals become attributes after imports
    manynames.f() # 11: manynames's X, not the one here!
    manynames.g() # 22: local in other file's function
    print(manynames.C.X) # 33: attribute of class in other module
    I = manynames.C()
    print(I.X) # 33: still from class here
    I.m()
    print(I.X) # 55: now from instance!