#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 21, 2017

@author: bob

One subtle point about the prior class-based coding is that while it works to intercept
simple function calls, it does not quite work when applied to class method functions:

When coded this way, the decorated method is rebound to an instance of the decorator
class, instead of a simple function.
The problem with this is that the self in the decorator¡¯s __call__ receives the
decorator class instance when the method is later run, and the instance of class C is
never included in *args. This makes it impossible to dispatch the call to the original
method¡ªthe decorator object retains the original method function, but it has no instance
to pass to it.
'''

class decorator:
    def __init__(self, func): # func is method without instance
        self.func = func
    def __call__(self, *args): # self is decorator instance
        pass# self.func(*args) fails! # C instance not in args!
    
class C:
    @decorator
    def method(self, x, y): # method = decorator(method)
        pass # Rebound to decorator instance

if __name__ == '__main__':
    pass