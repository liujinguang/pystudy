#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 21, 2017

@author: bob

This decorator is invoked at decoration time, and the callable it returns is invoked when
the original function name is later called. The decorator itself receives the decorated
function; the callable returned receives whatever arguments are later passed to the
decorated function¡¯s name. This works the same for class methods: the implied instance
object simply shows up in the first argument of the returned callable.

When the name func is later called, it really invokes the wrapper function returned by
decorator; the wrapper function can then run the original func because it is still available
in an enclosing scope. When coded this way, each decorated function produces a new
scope to retain state.
'''

def decorator(F):               #on @ decorations
    def wrapper(*args):         #on wrappted function call
        #use F and arps
        #F(*args) calls original function
        print args
        return F(*args)
        
    return wrapper

@decorator                      #func = decorator(func)
def func(x, y):                 #func is passed to decorator's F
    return x+y

if __name__ == '__main__':
    print func(6, 7)