#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月29日

@author: bob
'''

def foo(x):
    print "executing foo(%s)" % (x)
    
class A(object):
    def foo(self, x):
        print "executing foo(%s, %s)" % (self, x)
        
    @classmethod
    def class_foo(cls, x):
        print "executing class_foo(%s, %s)" % (cls, x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % (x)

if __name__ == '__main__':
    foo(5)
    
    a = A()
    a.foo(5)
    a.class_foo(5)
    a.static_foo(5)
    
    A.foo(a, 6)
    A.class_foo(6)
    A.static_foo(6)