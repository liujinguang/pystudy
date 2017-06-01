'''
Created on Jun 1, 2017

@author: bob
'''

class Borg(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        if cls not in Borg._state.keys():
            ob = super(Borg, cls).__new__(cls, *args, **kwargs)
            Borg._state[cls] = ob
        return Borg._state[cls]
    

class MyClass2(Borg):
    a = 1

if __name__ == '__main__':
    m1 = MyClass2()
    m2 = MyClass2()
    
    print m1 is m2
    print id(m1)
    print id(m2)