#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月30日

@author: bob
'''

if __name__ == '__main__':
    x = {'a':1, 'b': 2}
    y = {'b':10, 'c': 11}
    
    print x.items()
    z = dict(x.items() + y.items())
    print z
    
    