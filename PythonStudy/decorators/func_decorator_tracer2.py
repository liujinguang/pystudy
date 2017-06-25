#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 22, 2017

@author: bob

Unfortunately, moving the counter out to the common global scope to allow it to be
changed like this also means that it will be shared by every wrapped function. Unlike
class instance attributes, global counters are cross-program, not per-function¡ªthe
counter is incremented for any traced function call. You can tell the difference if you
compare this version¡¯s output with the prior version¡¯s¡ªthe single, shared global call
counter is incorrectly updated by calls to every decorated function:
'''

calls = 0

def tracer(func):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        
        print("call %s to %s" % (calls, func.__name__))
        return func(*args, **kwargs)

    return wrapper

@tracer
def spam(a, b, c): # Same as: spam = tracer(spam)
    print(a + b + c)
@tracer
def eggs(x, y): # Same as: eggs = tracer(eggs)
    print(x ** y)


if __name__ == '__main__':
    spam(1, 2, 3) # Really calls wrapper, bound to func
    spam(a=4, b=5, c=6) # wrapper calls spam
    eggs(2, 16) # Really calls wrapper, bound to eggs
    eggs(4, y=4) # Global calls is not per-function here!