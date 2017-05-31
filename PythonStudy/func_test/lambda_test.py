#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月31日

@author: bob
'''

def multipliers():
    return [lambda x : i * x for i in range(4)]

print [m(2) for m in multipliers()]

def multipliers_v1():
    for i in range(4):
        yield lambda x: i * x
        
print [m(2) for m in multipliers_v1()]

if __name__ == '__main__':
    pass