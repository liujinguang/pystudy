#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 21, 2017

@author: bob

When run under Python 2.6, __getattr__ does receive a variety of implicit attribute
fetches for built-in operations, because Python looks up such attributes in instances
normally. Conversely, __getattribute__ is not run for any of the operator overloading
names, because such names are looked up in classes only:
'''

class GetAttr:
    eggs = 88
    
    def __init__(self):
        self.spam = 77
        
    def __len__(self):
        print('__len__: 42')
        return 42
    
    def __getattr__(self, attr):
        print("getattr:" + attr)
        
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None
        
class GetAttribute(object):
    eggs = 88
    
    def __init__(self):
        self.spam = 77
        
    def __len__(self):
        print('__len__: 42')
        return 42   
    
    def __getattribute__(self, attr):
        print("getattribute:" + attr)
        
        if attr == '__str__':
            return lambda *args: '[Getattribute str]'
        else:
            return lambda *args: None    

if __name__ == '__main__':
    for Class in GetAttr, GetAttribute:
        print('\n' + Class.__name__.ljust(50, '='))
        X = Class()
        X.eggs # Class attr
        X.spam # Instance attr
        X.other # Missing attr
        len(X) # __len__ defined explicitly
        
        try: # New-styles must support [], +, call directly: redefine
            X[0] # __getitem__?
        except:
            print('fail []')
            
        try:
            X + 99 # __add__?
        except:
            print('fail +')
            
        try:
            X() # __call__? (implicit via built-in)
        except:
            print('fail ()')
            
        X.__call__() # __call__? (explicit, not inherited)
        print(X.__str__()) # __str__? (explicit, inherited from type)
        print(X) # __str__? (implicit via built-in)