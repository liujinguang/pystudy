#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 22, 2017

@author: bob

Notice how each function decorated with this class will create a new instance, with its
own saved function object and calls counter. Also observe how the *args argument
syntax is used to pack and unpack arbitrarily many passed-in arguments. This generality
enables this decorator to be used to wrap any function with any number of arguments
(this version doesn't yet work on class methods, but we'll fix that later in this
section).
'''

class Tracer(object):
    def __init__(self, func):
        self.calls = 0
        self.func = func
        
    def __call__(self, *args):
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))

@Tracer
def spam(a, b, c):          #spam = Tracer(spam), wraps spam in a decorator object
    print(a + b + c)


@Tracer
def add(a, b):
    return a+b

if __name__ == '__main__':
    for i in xrange(10):
        spam(1, 2, 3)
        
    for i in xrange(5):
        add(3, 4)