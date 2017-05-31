#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月30日

@author: bob
'''

def function(data=[]):
    data.append(5)
    return data

if __name__ == '__main__':
    print dir(function)
    print(id(function()))
    print(id(function()))
    print(id(function()))
