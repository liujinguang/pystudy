'''
Created on May 26, 2017

@author: bob
'''

class ObjectCreator(object):
    pass

def echo(o):
    print o

if __name__ == '__main__':
    my_object = ObjectCreator()
    
    print my_object
    
    #you can print a class because it's an object
    print ObjectCreator
    
    #you can pass a class a parameter
    echo(ObjectCreator)
    
    print(hasattr(ObjectCreator, 'new_attribute'))
    
    #you can add attributes to a class
    ObjectCreator.new_attribute = 'foo'
    print(hasattr(ObjectCreator, 'new_attribute'))
    
    ObjectCreatorMirror = ObjectCreator # you can assign a class to a variable
    print(ObjectCreatorMirror.new_attribute)
    
    print(ObjectCreatorMirror())
    
    print type(ObjectCreator)
    print type(ObjectCreator())