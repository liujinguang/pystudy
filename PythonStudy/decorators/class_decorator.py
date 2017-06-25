#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 22, 2017

@author: bob

Rather than
wrapping individual functions or methods, though, class decorators are a way to manage
classes, or wrap up instance construction calls with extra logic that manages or
augments instances created from a class.

In symbolic terms, assuming that
decorator is a one-argument function that returns a callable, the class decorator syntax:
    @decorator # Decorate class
    class C:
        ...
    x = C(99) # Make an instance
is equivalent to the following¡ªthe class is automatically passed to the decorator function,
and the decorator¡¯s result is assigned back to the class name:
    class C:
        ...
    C = decorator(C) # Rebind class name to decorator result
    x = C(99) # Essentially calls decorator(C)(99)
    '''


def decorator(cls):             #on @ decoration
    class Wrapper(object):
        def __init__(self, *args):      #on instance creation
            print "Wrapper.__init__"
            self.wrapped = cls(*args)
        def __getattr__(self, name):        #on attribute fecth
            print "Wrapper.__getattr__"
            return getattr(self.wrapped, name)
    
    return Wrapper

@decorator
class C(object):                    #C = decorator(C)
    def __init__(self, x, y):       #RUN BY Wrapper.__init__
        print "C.__init__"
        self.attr = 'spam'

if __name__ == '__main__':
    x = C(6, 7)                     #Really calls Wrapper(6, 7)
    print(x.attr)                   #runs Wrapper.__getattr__,