#!/usr/bin/python

'''
Created on May 16, 2017

@author: bob
'''

import sys

if __name__ == '__main__':
    #Python indexes start at Zero, so let's not count the command itself
    #which is sys.argv[0]
    num_arguments = len(sys.argv) - 1
    
    #if there are no arguments to the command, send a message to standard error
    if num_arguments == 0:
        print "Hi, type in an option silly"
    else:
        print sys.argv, "You typed in", num_arguments, "argumetns"
