#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 21, 2017

@author: bob
To support both functions and methods, the nested function alternative works better:

Technically, this nested-function version works because Python creates a bound
method object and thus passes the subject class instance to the self argument only
when a method attribute references a simple function; when it references an instance
of a callable class instead, the callable class¡¯s instance is passed to self to give the
callable class access to its own state information. We¡¯ll see how this subtle difference
can matter in more realistic examples later in this chapter.
'''

def decorator(F):           #F is function or method without instance
    def wrapper(*args):     #class instance in args[0] for method
        pass  #F(*args) runs func or method
    
    return wrapper

@decorator
def func(x, y):             #func = decorator(func)
    pass 

class C(object):
    #When coded this way wrapper receives the C class instance in its first argument, so it
    #can dispatch to the original method and access state information.
    @decorator
    def method(self, x, y):     #method = decorator(method), rebound to a simple function
        pass

if __name__ == '__main__':
    func(6, 8)
    
    x = C()
    x.method(6, 7)              # Really calls wrapper(X, 6, 7)