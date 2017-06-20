#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月20日

@author: bob

To do the same with descriptors, we define the attributes with complete classes. Note
that these descriptors store base values as instance state, so they must use leading underscores
again so as not to clash with the names of descriptors

'''

class DescSquare(object):
    def __get__(self, instance, owner):
        return instance._square ** 2
    
    def __set__(self, instance, value):
        instance._square = value
        
class DescCube(object):
    def __get__(self, instance, owner):
        return instance._cube ** 3
    
class Powers(object):
    square = DescSquare()
    cube = DescCube()
    
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

if __name__ == '__main__':
    X = Powers(3, 4)
    print(X.square) # 3 ** 2 = 9
    print(X.cube) # 4 ** 3 = 64
    X.square = 5
    print(X.square) # 5 ** 2 = 25