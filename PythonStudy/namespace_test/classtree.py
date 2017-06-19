#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月19日

@author: bob

climb inheritance trees using namespace link
displaying higher superclasses with indentation
'''

def classtree(cls, indent):
    print('.' * indent + cls.__name__)          #print class name here
    for supercls in cls.__bases__:              #recur to all superclasses
        classtree(supercls, indent+3)           #may visit super > once
        
def instancetree(inst):
    print('Tree of %s' % inst)                  #show instance
    classtree(inst.__class__, 3)                #climb to its class

class A: pass
class B(A): pass
class C(A): pass
class D(B,C): pass
class E: pass
class F(D,E): pass


if __name__ == '__main__':
    instancetree(F())