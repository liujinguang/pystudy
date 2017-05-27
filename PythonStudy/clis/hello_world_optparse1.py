#!/usr/bin/env python
'''
Created on May 16, 2017

@author: bob
'''

import optparse

def main():
    p = optparse.OptionParser()
    p.add_option("--sysadmin", "-s", default="BOFH")
    
    options, arguments = p.parse_args()
    print 'Hello, %s' % options.sysadmin

if __name__ == '__main__':
    main()