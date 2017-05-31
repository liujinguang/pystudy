'''
Created on May 27, 2017

@author: bob
'''

class DescState(object):
    def __init__(self, value):
        self.value = value
        
    def __get__(self, instance, owner):
        print("DescState get")
        return self.value * 10
    
    def __set__(self, instance, value):
        print("DescState set")
        self.value = value
        
class CalcAttrs(object):
    X = DescState(2)
    Y = 3
    def __init__(self):
        self.Z = 4

if __name__ == '__main__':
    obj = CalcAttrs()
    print(obj.X, obj.Y, obj.Z)
    obj.X = 5
    obj.Y = 6
    obj.Z = 7
    print(obj.X, obj.Y, obj.Z)