#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017��5��29��

@author: bob
'''

import optparse
import os

def main():
    p = optparse.OptionParser(description="Lists content of two directories",
                              prog="pymultils",
                              version="0.1a",
                              usage="%prog [--dir dir1 dir2]")
    p.add_option("--dir", action="store", dest="dir", nargs=2)
    options, arguments = p.parse_args()
    if options.dir:
        for dir in options.dir:
            print "Listing of %s\n" % dir
            
            for filename in os.listdir(dir):
                print "    %s" % filename
    else:
        p.print_help()

if __name__ == '__main__':
    main()