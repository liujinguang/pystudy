#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月20日

@author: bob
'''

class AttrSquare(object):
    def __init__(self, start):
        self.value = start
        
    def __getattr__(self, attr):            #On undefined attr fetch
        if attr == 'X':
            return self.value ** 2
        else:
            raise AttributeError(attr)
        
    def __setattr__(self, attr, value):
        if attr == 'X':
            attr = 'value'
        self.__dict__[attr] = value

if __name__ == '__main__':
    A = AttrSquare(3) # 2 instances of class with overloading
    B = AttrSquare(32) # Each has different state information
    print(A.X) # 3 ** 2
    A.X = 4
    print(A.X) # 4 ** 2
    print(B.X) # 32 ** 2