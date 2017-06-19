#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 19, 2017

@author: bob

An abstract superclass is a class that calls a method, but does not inherit or define
it—it expects the method to be filled in by a subclass. This is often used as a way
to generalize classes when behavior cannot be predicted until a more specific subclass
is coded. OOP frameworks also use this as a way to dispatch to client-defined,
customizable operations.
'''

class Super(object):
    def method(self):  #default behavior
        print('in Super.method')
        
    def delegate(self):   #Expected to be defined
        self.action()
        
    def action(self):   #Abstract Superclasses
        raise NotImplementedError("action must be defined")
        
class Inheritor(Super):  #inherit method verbatim
    pass

class Replacer(Super):  #replace method completely
    def method(self):
        print('in Replacer.method')

class Extender(Super):  #extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('End Extender.method')

class Provider(Super):
    #When we call the delegate method through a Provider instance, two independent 
    #inheritance searches occur:
    #1. On the initial x.delegate call, Python finds the delegate method in Super by
    #searching the Provider instance and above. The instance x is passed into the
    #method¡¯s self argument as usual.
    #2. Inside the Super.delegate method, self.action invokes a new, independent inheritance
    #search of self and above. Because self references a Provider instance,
    #the action method is located in the Provider subclass.
    def action(self):
        print('in Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        #Classes also have the special __name__ attribute, like modules; it¡¯s preset to a
        #string containing the name in the class header.
        print("\n" + klass.__name__ + "...")
        klass().method()
        
    
    x = Provider()
    x.delegate()