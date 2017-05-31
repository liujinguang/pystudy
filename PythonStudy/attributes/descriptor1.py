'''
Created on May 27, 2017

@author: bob
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