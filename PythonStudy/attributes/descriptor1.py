'''
Created on May 27, 2017

@author: bob
Unlike with properties, however, omitting a __set__ allows the name to be redefined in an instance,
thereby hiding the descriptor¡ªto make an attribute read-only, you must define
__set__ to catch assignments and raise an exception.
'''

class D(object):
    def __get__(self, *args):
        print("get")
        
    def __set__(self, *args):
        raise AttributeError('cannot set')
        
class C(object):
    a = D()

if __name__ == '__main__':
    x = C()
    x.a 
    print(list(x.__dict__.keys()))
    x.a = 99
    print(list(x.__dict__.keys()))