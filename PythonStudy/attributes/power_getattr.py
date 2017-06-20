#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月20日

@author: bob
'''

class Powers(object):
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
        
    def __getattr__(self, attr):
        if attr == 'square':
            return self._square ** 2
        elif attr == 'cube':
            return self._cube ** 3
        else:
            raise AttributeError('Unknown attr:' + attr)
        
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