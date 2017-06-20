#/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on May 27, 2017

@author: bob

Functionally speaking, the descriptor protocol allows us to route a specific attribute¡¯s
get and set operations to methods of a separate class object that we provide: they provide
a way to insert code to be run automatically on attribute access, and they allow us
to intercept attribute deletions and provide documentation for the attributes if desired.
Descriptors are created as independent classes, and they are assigned to class attributes
just like method functions. Like any other class attribute, they are inherited by subclasses
and instances. Their access-interception methods are provided with both a
self for the descriptor itself, and the instance of the client class. Because of this, they
can retain and use state information of their own, as well as state information of the
subject instance. For example, a descriptor may call methods available in the client
class, as well as descriptor-specific methods it defines.
Like a property, a descriptor manages a single, specific attribute; although it can¡¯t catch
all attribute accesses generically, it provides control over both fetch and assignment
accesses and allows us to change an attribute freely from simple data to a computation
without breaking existing code.
'''

'''
Like a property, a descriptor manages a single, specific attribute; although it can¡¯t catch
all attribute accesses generically, it provides control over both fetch and assignment
accesses and allows us to change an attribute freely from simple data to a computation
without breaking existing code.
'''
# class Descriptor:
#     "docstring goes here"
#     def __get__(self, instance, owner): ... # Return attr value
#     def __set__(self, instance, value): ... # Return nothing (None)
#     def __delete__(self, instance): ... # Return nothing (None)

class Descriptor(object):
    def __get__(self, instance, owner):
        print(self, instance, owner)
        
        
class Subject(object):
    attr = Descriptor()

if __name__ == '__main__':
    X = Subject()
    
    X.attr