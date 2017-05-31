'''
Created on May 27, 2017

@author: bob
'''

class PropSquare(object):
    def __init__(self, start):
        self.value = start
        
    def getX(self):
        return self.value ** 2
    
    def setX(self, value):
        self.value = value
        
    X = property(getX, setX)


if __name__ == '__main__':
    p = PropSquare(3)
    print p.X
    p.setX(4)
    print p.X