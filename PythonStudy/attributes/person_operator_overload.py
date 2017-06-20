#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月20日

@author: bob

Because they are generic,
__getattr__ and __getattribute__ are probably more commonly used in delegationbase
code (as sketched earlier), where attribute access is validated and routed to an
embedded object. Where just a single attribute must be managed, properties and descriptors
might do as well or better.
'''

class Person(object):
    def __init__(self, name):
        #Notice that the attribute assignment in the __init__ constructor triggers __setattr__
        #too—this method catches every attribute assignment, even those within the class itself.
        self._name = name
        
    def __getattr__(self, attr):
        if attr == 'name':
            print("fetch...")
            return self._name               # Does not loop: real attr
        else:
            raise AttributeError(attr)
        
    def __getattribute__(self, attr):
        if attr == 'name':
            print("fetch...")
            return self._name               # Does not loop: real attr
        return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):
        if attr == 'name':
            print('change...')
            attr = '_name'
            
        print("..........")
        self.__dict__[attr] = value         # Avoid looping here
        
    def __delattr__(self, attr):
        if attr == 'name':
            print('remove...')
            attr = '_name'                  # Avoid looping here too
            
        del self.__dict__[attr]             

if __name__ == '__main__':
    bob = Person('Bob Smith')       # bob has a managed attribute
    print(bob.name)                 # Runs __getattr__
    bob.name = 'Robert Smith'       # Runs __setattr__
    print(bob.name)
    del bob.name                    # Runs __delattr__
    
    print('-'*20)
    sue = Person('Sue Jones') # sue inherits property too
    print(sue.name)