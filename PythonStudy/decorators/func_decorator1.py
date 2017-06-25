#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 21, 2017

@author: bob

When the name func is later called now, it really invokes the __call__ operator overloading
method of the instance created by decorator; the __call__ method can then
run the original func because it is still available in an instance attribute. When coded
this way, each decorated function produces a new instance to retain state.
'''

class decorator(object):
    def __init__(self, func):       #on @decoration
        self.func = func
        
    def __call__(self, *args):      #on wrapped function call
        #Use self.func and args
        #self.func(*args) call original function
        print args
        return self.func(*args)

@decorator
def func(x, y):                     #func = docrator(func)
    return x + y                    #func is passed to __init__


if __name__ == '__main__':
    print func(6, 7)