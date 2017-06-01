'''
Created on May 31, 2017

@author: bob
'''

from __future__ import division

def div1(x,y):
    print "%s/%s = %s" % (x, y, x/y)

def div2(x,y):
    print "%s//%s = %s" % (x, y, x//y)


if __name__ == '__main__':
    div1(5,2)
    div1(5.,2)
    div2(5,2)
    div2(5.,2.)