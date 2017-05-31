#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月31日

@author: bob
'''

if __name__ == '__main__':
    lst = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]
    print [x for x in lst[::2] if x%2 == 0]
    print lst[::-1]
    
    print xrange(10)