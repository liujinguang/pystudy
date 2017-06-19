#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月19日

@author: bob
'''

import docstr

if __name__ == '__main__':
    print docstr.__file__
    
    print "#" * 50
    print docstr.__doc__
    
    print "#" * 50
    print docstr.func.__doc__
    
    print "#" * 50
    print docstr.spam.__doc__
    
    print "#" * 50
    print docstr.spam.method.__doc__