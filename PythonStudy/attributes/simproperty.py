'''
Created on May 27, 2017

@author: bob
'''

# This Property class catches attribute accesses with the descriptor protocol and routes
# requests to functions or methods passed in and saved in descriptor state when the class
# is created. Attribute fetches, for example, are routed from the Person class, to the
# Property class¡¯s __get__ method, and back to the Person class¡¯s getName. With descriptors,
# this ¡°just works.¡±

# Note that this descriptor class equivalent only handles basic property usage, though;
# to use @ decorator syntax to also specify set and delete operations, our Property class
# would also have to be extended with setter and deleter methods, which would save
# the decorated accessor function and return the property object (self should suffice).

class Property(object):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc
        
    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        
        if self.fget is None:
            raise AttributeError("can't get attribute")
        
        return self.fget(instance)
    
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        
        self.fset(instance, value)
        
    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        
        self.fdel(instance)
        

class Person(object):
    def __init__(self, name):
        self._name = name
        
    def getName(self):
        print('fecth...')
        return self._name
    
    def setName(self, value):
        print('change...')
        self._name = value
        
    def delName(self):
        print('remove...')
        del self._name
        
    name = Property(getName, setName, delName)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    
    print(bob.name) # Runs getName
    bob.name = 'Robert Smith' # Runs setName
    print(bob.name)
    del bob.name # Runs delName