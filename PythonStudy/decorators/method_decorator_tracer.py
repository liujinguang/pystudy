#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 22, 2017

@author: bob

The root of the problem here is in the self argument of the tracer class¡¯s __call__
method¡ªis it a tracer instance or a Person instance? We really need both as it¡¯s coded:
the tracer for decorator state, and the Person for routing on to the original method.
Really, self must be the tracer object, to provide access to tracer¡¯s state information;
this is true whether decorating a simple function or a method.
Unfortunately, when our decorated method name is rebound to a class instance object
with a __call__, Python passes only the tracer instance to self; it doesn¡¯t pass along
the Person subject in the arguments list at all. Moreover, because the tracer knows
nothing about the Person instance we are trying to process with method calls, there¡¯s
no way to create a bound method with an instance, and thus no way to correctly dispatch
the call.
'''

class tracer(object):
    def __init__(self, func):       #state via instance attributes
        self.calls = 0
        self.func = func
        
       
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

@tracer
def spam(a, b, c):      # Same as: spam = tracer(spam)
    print(a + b + c)    # Triggers tracer.__init__


class Person(object):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    
    @tracer
    def giveRaise(self, percent):           #giveRaise = tracer(giveRaise)
        self.pay *= (1.0 + percent)
        
    @tracer
    def lastName(self):
        return self.name.split()[-1]

if __name__ == '__main__':
    spam(1, 2, 3) # Runs tracer.__call__
    spam(a=4, b=5, c=6) # spam is an instance attribute    
    
    bob = Person('Bob Smith', 50000) # tracer remembers method funcs
    bob.giveRaise(.25) # Runs tracer.__call__(???, .25)
    print(bob.lastName()) # Runs tracer.__call__(???)    
    