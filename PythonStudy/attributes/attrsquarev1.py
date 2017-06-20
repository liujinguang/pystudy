#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月20日

@author: bob

As before, we can achieve the same effect with __getattribute__ instead of
__getattr__; the following replaces the fetch method with a __getattribute__ and
changes the __setattr__ assignment method to avoid looping by using direct superclass
method calls instead of __dict__ keys:
'''

class AttrSquare(object):
    '''
    Notice the implicit routing going on in inside this class’s methods:
    • self.value=start inside the constructor triggers __setattr__
    • self.value inside __getattribute__ triggers __getattribute__ again
    In fact, __getattribute__ is run twice each time we fetch attribute X. This doesn’t happen
    in the __getattr__ version, because the value attribute is not undefined. If you care
    about speed and want to avoid this, change __getattribute__ to use the superclass to
    fetch value as well:
        def __getattribute__(self, attr):
            if attr == 'X':
                return object.__getattribute__(self, 'value') ** 2    
    '''
    def __init__(self, start):
        self.value = start
        
    def __getattribute__(self, attr):
        if attr == 'X':
            return self.value ** 2              # Triggers __getattribute__ again!
        else:
            return object.__getattribute__(self, attr)
        
    def __setattr__(self, attr, value):
        if attr == 'X':
            attr = 'value'
            
        object.__setattr__(self, attr, value)

if __name__ == '__main__':
    A = AttrSquare(3) # 2 instances of class with overloading
    B = AttrSquare(32) # Each has different state information
    print(A.X) # 3 ** 2
    A.X = 4
    print(A.X) # 4 ** 2
    print(B.X) # 32 ** 2