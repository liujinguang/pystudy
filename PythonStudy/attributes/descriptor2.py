'''
Created on May 27, 2017

@author: bob

Also note that when a descriptor class is not useful outside the client class, it¡¯s perfectly
reasonable to embed the descriptor¡¯s definition inside its client syntactically.

Also note that when a descriptor class is not useful outside the client class, it?¡¥s perfectly
reasonable to embed the descriptor?¡¥s definition inside its client syntactically.
'''

# In fact, descriptors can use both instance state and descriptor state, or any combination thereof:
# ? Descriptor state is used to manage data internal to the workings of the descriptor.
# ? Instance state records information related to and possibly created by the client class.
        
class Person(object):
    def __init__(self, name):
        self._name = name
        
    class Name(object):
        "name descriptor docs"
        def __get__(self, instance, owner):
            """
            When the descriptor¡¯s __get__ method is run, it is passed three objects to define its context:
            ? self is the Name class instance.
            ? instance is the Person class instance.
            ? owner is the Person class.
            """
            print("fetch...")
            return instance._name
        
        def __set__(self, instance, value):
            print("change...")
            instance._name = value
            
        def __delete__(self, instance):
            print("remove...")
            del instance._name    
        
    name = Name()

if __name__ == '__main__':
    bob = Person('Bob Smith') # bob has a managed attribute
    print(bob.name) # Runs Name.__get__
    bob.name = 'Robert Smith' # Runs Name.__set__
    print(bob.name)
    del bob.name # Runs Name.__delete__
    print('-'*20)