#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 21, 2017

@author: bob
'''

class Powers(object):
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
        
    def __getattribute__(self, attr):
        # route base value fetches to a superclass to avoid looping
        if attr == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif attr == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, attr)
        
    def __setattr__(self, attr, value):
        if attr == 'square':
            self.__dict__['_square'] = value
        else:
            self.__dict__[attr] = value
        

if __name__ == '__main__':
    X = Powers(3, 4)
    print(X.square) # 3 ** 2 = 9
    print(X.cube) # 4 ** 3 = 64
    X.square = 5
    print(X.square) # 5 ** 2 = 25