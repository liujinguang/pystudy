#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月30日

@author: bob
'''

def enum(**enums):
    return type('Enum', (), enums)

if __name__ == '__main__':
    Numbers = enum(ONE=1, TWO=2, THREE="THREE")
    print Numbers.ONE
    print Numbers.TWO