#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 20, 2017

@author: bob

refer descriptor2.py

Notice in this code how we assign an instance of our descriptor class to a class attribute
in the client class; because of this, it is inherited by all instances of the class, just
like a class¡¯s methods. Really, we must assign the descriptor to a class attribute like
this¡ªit won¡¯t work if assigned to a self instance attribute instead.


'''

class Name(object):
    "name descriptor docs"
    def __get__(self, instance, owner):
        print("fetch...")
        return instance._name
    
    def __set__(self, instance, value):
        print("change...")
        instance._name = value
        
    def __delete__(self, instance):
        print("remove...")
        del instance._name
        
class Person(object):
    def __init__(self, name):
        self._name = name
    
    #Also like the property example, our descriptor class instance is a class attribute and 
    #thus is inherited by all instances of the client class and any subclasses.
    name = Name()

if __name__ == '__main__':
    bob = Person("Bob Smith")
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    print dir(bob)
    del bob.name