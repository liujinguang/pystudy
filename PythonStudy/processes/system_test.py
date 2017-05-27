#!/usr/bin/python

'''
Created on May 13, 2017

@author: bob
'''

import os

if __name__ == '__main__':
    result = os.system("ls /etc/network")
    
    print "result=%d" % result