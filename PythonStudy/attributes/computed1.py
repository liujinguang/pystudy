'''
Created on May 27, 2017

@author: bob
'''

class DescSquare(object):
    def __init__(self, start):
        self.value = start
        
    def __get__(self, instance, owner):
        return self.value ** 2
    
    def __set__(self, instance, value):
        self.value = value

class Client1(object):
    X = DescSquare(3)

if __name__ == '__main__':
    c1 = Client1()
    print(c1.X)
    c1.X = 4
    
    print(c1.X)