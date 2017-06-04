'''
Created on Jun 4, 2017

@author: bob
'''

def foo(x, y):
    print x, y

if __name__ == '__main__':
    point_foo = (3,4)
    point_bar = {'x':3, 'y':4}
    foo(*point_foo)
    foo(**point_bar)