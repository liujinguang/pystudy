#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 22, 2017

@author: bob

We use lambda functions to implement wrapper layers here (each retains the wrapped
function in an enclosing scope); in practice, wrappers can take the form of functions,
callable classes, and more. When designed well, decorator nesting allows us to combine
augmentation steps in a wide variety of ways.
'''

def d1(F):
    return lambda: 'X' + F()

def d2(F):
    return lambda: 'Y' + F()


def d3(F):
    return lambda: 'Z' + F()

@d1
@d2
@d3
def func():
    return 'spam'

if __name__ == '__main__':
    print func()