#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 19, 2017

@author: bob

refer specialize.py

As of Python 2.6 and 3.0, the prior section¡¯s abstract superclasses (a.k.a. ¡°abstract base
classes¡±), which require methods to be filled in by subclasses, may also be implemented
with special class syntax.

'''

from abc import ABCMeta, abstractmethod


class Super(object):
    __metaclass__ = ABCMeta
    def method(self):  #default behavior
        print('in Super.method')
        
    def delegate(self):   #Expected to be defined
        self.action()
    
    @abstractmethod
    def action(self):   #Abstract Superclasses
        pass 

class Inheritor(Super):  #inherit method verbatim
    pass

class Provider(Super):
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    '''
    Coded this way, a class with an abstract method cannot be instantiated (that is, we
    cannot create an instance by calling it) unless all of its abstract methods have been
    defined in subclasses. Although this requires more code, the advantage of this approach
    is that errors for missing methods are issued when we attempt to make an instance of
    the class, not later when we try to call a missing method. This feature may also be used
    to define an expected interface, automatically verified in client classes.
    '''
    x = Provider()
    x.delegate()
    
    y = Inheritor()
    y.delegate()