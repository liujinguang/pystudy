#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月30日

@author: bob
'''

import enum

if __name__ == '__main__':
    animal = enum.Enum("Animal", "ant bee cat dog")
    print animal.ant
    print animal.bee