'''
Created on May 26, 2017

@author: bob
'''

#remember that 'type' is actually a class like 'str' and 'int'
#so you can inherit from it
class UpperAttrMetaClass(type):
    # __new__ is the method called before __init__
    # it's the method that creates the object and returns it
    # while __init__ just initializes the object passed as parameter
    # you rarely use __new__, except when you want to control how the object
    # is created.
    # here the created object is the class, and we want to customize it
    # so we override __new__
    # you can do some stuff in __init__ too if you wish
    # some advanced use involves overriding __call__ as well, but we won't
    # see this
    def __new__(cls, future_class_name, future_class_parents, 
                future_class_attr):
        
        uppercase_attr = {}
        
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
                
        return type.__new__(cls, future_class_name, 
                            future_class_parents, future_class_attr)

if __name__ == '__main__':
    pass