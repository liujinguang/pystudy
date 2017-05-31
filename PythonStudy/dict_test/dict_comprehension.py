#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月29日

@author: bob
'''

if __name__ == '__main__':
    lst = [("aaa", "bbb"), ("ccc", "ddd")]
    
    d = { key:value for (key, value) in lst}
    print d