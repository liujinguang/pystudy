'''
Created on May 27, 2017

@author: bob
    @decorator
    def func(args): ...
is automatically translated to this equivalent by Python, to rebind the function name
to the result of the decorator callable:
    def func(args): ...
    func = decorator(func)

'''

class Person(object):
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        'name property docs'
        print("fecth...")
        return self._name
    
    @name.setter
    def name(self, value):
        print("change...")
        self._name = value
    
    @name.deleter
    def name(self):
        print('remove...')
        del self._name

if __name__ == '__main__':
    bob = Person('Bob Smith') # bob has a managed attribute
    print(bob.name) # Runs name getter (name 1)
    bob.name = 'Robert Smith' # Runs name setter (name 2)
    print(bob.name)
    del bob.name # Runs name deleter (name 3)
    print('-'*20)
    sue = Person('Sue Jones') # sue inherits property too
    print(sue.name)
    print(Person.name.__doc__) # Or help(Person.name)