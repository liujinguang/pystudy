#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月11日

@author: bob
'''

class DefaultDict(dict):
    def __missing__(self, key):
        return []
    
if __name__ == '__main__':
    d = DefaultDict()
    print d['florp']
    d['florp'] = d['florp'].append(127)
    
    print d
    
    lst = [ ]
    lst.append(1)
    print lst