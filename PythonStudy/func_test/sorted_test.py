#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月30日

@author: bob
'''

if __name__ == '__main__':
    import operator
    x = {1: 2, 3: 4, 4:3, 2:1, 0:0}
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    print sorted_x