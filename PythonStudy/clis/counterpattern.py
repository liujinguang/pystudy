#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017��528日

@author: bob
'''

import optparse
import os

def main():
    p = optparse.OptionParser(description="Python 'ls' command clone",
                              prog="pyls", version="0.1a",
                              usage="%prog [directory]")
    p.add_option("-v", action="count", dest="verbose")
    options, arguments = p.parse_args()
    if len(arguments) == 1:
        if options.verbose:
            print "Verbose mode enable at level: %s" % options.verbose
            
        path = arguments[0]
        for filename in os.listdir(path):
            if options.verbose == 1:
                print filename
            elif options.verbose == 2:
                print "Filename: %s" % filename
            else:
                fullpath = os.path.join(path, filename)
                print "Filename: %s | Byte Size: %s" % (filename, os.path.getsize(fullpath))
            
    else:
        p.print_help()

if __name__ == '__main__':
    main()