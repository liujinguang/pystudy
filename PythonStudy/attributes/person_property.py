'''
Created on May 27, 2017

@author: bob

The property protocol allows us to route a specific attribute's get and set operations to
functions or methods we provide, enabling us to insert code to be run automatically
on attribute access, intercept attribute deletions, and provide documentation for the
attributes if desired.
Properties are created with the property built-in and are assigned to class attributes,
just like method functions. As such, they are inherited by subclasses and instances, like
any other class attributes. Their access-interception functions are provided with the
self instance argument, which grants access to state information and class attributes
available on the subject instance.
A property manages a single, specific attribute; although it can't catch all attribute
accesses generically, it allows us to control both fetch and assignment accesses and
enables us to change an attribute from simple data to a computation freely, without
breaking existing code.
'''

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
        
    name = property(getName, setName, delName, "name property docs")
    
class Student(Person):
    pass

if __name__ == '__main__':
    bob = Person('Bob Smith')
    
    print(bob.name) # Runs getName
    bob.name = 'Robert Smith' # Runs setName
    print(bob.name)
    del bob.name # Runs delName
    print('-'*20)
    sue = Person('Sue Jones') # sue inherits property too
    print(sue.name)
    print(Person.name.__doc__) # Or help(Person.name)
    print('-'*20)
    stu = Student('Will Emerson')
    print stu.name