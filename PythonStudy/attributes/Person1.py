'''
Created on May 27, 2017

@author: bob
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