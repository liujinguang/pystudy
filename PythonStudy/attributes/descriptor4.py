'''
Created on May 27, 2017

@author: bob
'''

class InstState(object):
    def __get__(self, instance, owner):
        print("InstState get")
        return instance._Y * 100
    
    def __set__(self, instance, value):
        print("InstState set")
        instance._Y = value
        
class CalcAttrs(object):
    Y = InstState()
    X = 3
    
    def __init__(self):
        self._Y = 3
        self.Z = 4

if __name__ == '__main__':
    obj = CalcAttrs()
    print(obj.X, obj.Y, obj.Z) # X and Y are computed, Z is not
    obj.X = 5 # X and Y assignments intercepted
    obj.Y = 6
    obj.Z = 7
    print(obj.X, obj.Y, obj.Z)