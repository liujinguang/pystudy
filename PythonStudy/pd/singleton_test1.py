'''
Created on Jun 1, 2017

@author: bob
'''

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            print cls
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance
    
class MyClass(Singleton):
    a = 1

if __name__ == '__main__':
    my1 = MyClass()
    my2 = MyClass()
    
    print my1 is my2
    print my1 == my2