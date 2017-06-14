#!/usr/bin/env python
'''
Created on Jun 4, 2017

@author: bob
'''

# import this

if __name__ == '__main__':
#     n = ((a,b) for a in range(0,2) for b in range(4,6))
#     print n
    
    for i in xrange(1, 511):
        if i in [252, 253, 254]:
            continue
        
        if i < 256:
            print "127.11.%d.x" % i
        else:
            print "127.10.%d.x" % (i - 255)