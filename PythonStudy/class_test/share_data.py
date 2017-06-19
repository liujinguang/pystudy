'''
Created on Jun 19, 2017

@author: bob
'''

class SharedData(object):
    spam = 42
    
#Assignments to instance attributes create or change the names in the instance, rather
#than in the shared class. More generally, inheritance searches occur only on attribute
#references, not on assignment: assigning to an object?¡¥s attribute always changes that
#object, and no other.

if __name__ == '__main__':
    x = SharedData()
    y = SharedData()
    
    print x.spam, y.spam
    
    SharedData.spam = 99
    print x.spam, y.spam, SharedData.spam
    
    x.spam = 88
    print x.spam, y.spam, SharedData.spam
    