#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月31日

@author: bob
'''

if __name__ == '__main__':
    f = open("file_read.py")
#     aa = f.read()
#     print aa
#     f.close()
    
    for l in f.readlines():
        print l