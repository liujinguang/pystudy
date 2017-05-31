#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月30日

@author: bob
'''

def print_everything(*args):
    for count, thing in enumerate(args):
        print "{0}. {1}".format(count, thing)
        

def table_things(**kargs):
    for name, value in kargs.items():
        print '{0} = {1}'.format(name, value)

if __name__ == '__main__':
    print_everything("apple", "banana", "cabbage")
    table_things(apple="fruit", cabbage='vegetable')