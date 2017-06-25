#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 22, 2017

@author: bob

adds support
for keyword arguments and returns the wrapped function¡¯s result to support more use
cases:

Like the original, this uses class instance attributes to save state explicitly. Both the
wrapped function and the calls counter are per-instance information¡ªeach decoration
gets its own copy

While useful for decorating functions, this coding scheme has issues when applied to
methods (more on this later).
'''

class tracer(object):
    def __init__(self, func):       #state via instance attributes
        self.calls = 0
        self.func = func
        
       
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

@tracer
def spam(a, b, c):      # Same as: spam = tracer(spam)
    print(a + b + c)    # Triggers tracer.__init__
    
@tracer
def eggs(x, y): # Same as: eggs = tracer(eggs)
    print(x ** y) # Wraps eggs in a tracer object


if __name__ == '__main__':
    spam(1, 2, 3) # Really calls tracer instance: runs tracer.__call__
    spam(a=4, b=5, c=6) # spam is an instance attribute
    eggs(2, 16) # Really calls tracer instance, self.func is eggs
    eggs(4, y=4) # self.calls is per-function here (need 3.0 nonlocal)