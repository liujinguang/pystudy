#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月30日

@author: bob
'''

class MyClass():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", world"

if __name__ == '__main__':
    mc = MyClass()
    print dir(mc)
#     print mc.__superprivate