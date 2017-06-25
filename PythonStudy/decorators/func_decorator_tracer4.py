#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 22, 2017

@author: bob

if you are not using Python 3.X and don?¡¥t have a nonlocal statement, you may
still be able to avoid globals and classes by making use of function attributes for some
changeable state instead. In recent Pythons, we can assign arbitrary attributes to functions
to attach them, with func.attr=value.

If you want your function decorators to work on both simple functions and class methods,
the most straightforward solution lies in using one of the other state retention
solutions described earlier?acode your function decorator as nested defs, so that you
don?¡¥t depend on a single self instance argument to be both the wrapper class instance
and the subject class instance.

'''

def tracer(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print("call %s to %s" % (wrapper.calls, func.__name__))
        return func(*args, **kwargs)        
        
    wrapper.calls = 0
    
    return wrapper

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

@tracer
def spam(a, b, c): # Same as: spam = tracer(spam)
    print(a + b + c)
@tracer
def eggs(x, y): # Same as: eggs = tracer(eggs)
    print(x ** y)


if __name__ == '__main__':
    spam(1, 2, 3) # Really calls wrapper, bound to func
    spam(a=4, b=5, c=6) # wrapper calls spam
    eggs(2, 16) # Really calls wrapper, bound to eggs
    eggs(4, y=4) # Global calls is not per-function here!
    
    print('methods...')
    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10) # Runs onCall(sue, .10)
    print(sue.pay)
    print(bob.lastName(), sue.lastName()) # Runs onCall(bob), lastName in scopes    
