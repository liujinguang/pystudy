#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月19日

@author: bob
'''

class Super(object):
    '''
    As classes assign to self attributes, they populate the instance objects—that is, attributes
    wind up in the instances’ attribute namespace dictionaries, not in the classes’.
    An instance object’s namespace records data that can vary from instance to instance,
    and self is a hook into that namespace:
    '''
    def hello(self):
        self.data1 = 'spam'
        
class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'

if __name__ == '__main__':
    x = Sub()           #instance namespace dict
    print x.__dict__
    
    print x.__class__   #class of instance
    
    print Sub.__bases__   #superclasses of class
    
    print Super.__bases__   #
    
    '''
    Also, observe that Y, a second instance made at the start of this series, still has an empty
    namespace dictionary at the end, even though X’s dictionary has been populated by
    assignments in methods. Again, each instance has an independent namespace dictionary,
    which starts out empty and can record completely different attributes than
    those recorded by the namespace dictionaries of other instances of the same class.
    '''
    print "=" * 50
    y = Sub()
    
    x.hello()
    print x.__dict__
    x.hola()
    print x.__dict__
    print Sub.__dict__.keys()
    print Super.__dict__.keys()
    
    print y.__dict__
    
    '''
    Because attributes are actually dictionary keys inside Python, there are really two ways
    to fetch and assign their values—by qualification, or by key indexing:
    '''
    print "=" * 50
    print x.data1, x.__dict__['data1']
    x.data3 = 'toast'
    print x.__dict__
    x.__dict__['data3'] = 'ham'
    print x.__dict__
    '''
    This equivalence applies only to attributes actually attached to the instance, though.
    Because attribute fetch qualification also performs an inheritance search, it can access
    attributes that namespace dictionary indexing cannot. The inherited attribute
    X.hello, for instance, cannot be accessed by X.__dict__['hello'].
    '''
    ########################################################################
    '''
    built-in dir function work on class and instance objects. This function works on anything
    with attributes: dir(object) is similar to an object.__dict__.keys() call. Notice, though, 
    that dir sorts its list and includes some system attributes
    '''
    print "=" * 50
    print x.__dict__, y.__dict__
    print list(x.__dict__.keys())
    print dir(x)
    print dir(Sub)
    