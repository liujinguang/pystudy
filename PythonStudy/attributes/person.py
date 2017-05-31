'''
Created on May 27, 2017

@author: bob
'''

class Person(object):
    def valid(self):
        return True
    
    def transform(self, val):
        return val
    
    def getName(self):
        if not self.valid():
            raise TypeError('cannot fetch name')
        else:
            return self.name.transform()
        
    def setName(self, value):
        if not self.valid():
            raise TypeError('cannot change name')
        else:
            self.name = self.transform(value)
        

if __name__ == '__main__':
    person = Person()
    person.getName()
    person.setName('value')