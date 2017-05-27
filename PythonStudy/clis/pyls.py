#!/usr/bin/env python

'''
Created on May 17, 2017

@author: bob
'''

import optparse
import os

def main():
    p = optparse.OptionParser(description="Python 'ls' command clone", 
                              prog="pyls", version="0.1a", 
                              usage="%prog [directory]")
    
    options, arguments = p.parse_args()
    
    #check the argument number, only accept one argument
    if len(arguments) == 1: 
        path = arguments[0]
        
        for filename in os.listdir(path):
            print filename
    else:
        #print help information
        p.print_help()

if __name__ == '__main__':
    main()