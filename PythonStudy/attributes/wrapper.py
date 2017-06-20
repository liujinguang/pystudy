#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月20日

@author: bob
Such a coding structure can be used to implement the delegation design pattern
Because all attribute are routed to our interception methods
generically, we can validate and pass them along to embedded, managed objects. The
following class (borrowed from Chapter 30), for example, traces every attribute fetch
made to another object passed to the wrapper class:
'''

class Wrapper(object):
    def __init__(self, obj):
        self.wrapped = obj
        
    def __getattr__(self, attrname):
        print('Trace', attrname)
        return getattr(self.obj, attrname)

if __name__ == '__main__':
    pass