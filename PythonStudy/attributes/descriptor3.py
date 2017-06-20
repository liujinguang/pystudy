'''
Created on May 27, 2017

@author: bob

In fact, descriptors can use both instance
state and descriptor state, or any combination thereof:
? Descriptor state is used to manage data internal to the workings of the descriptor.
? Instance state records information related to and possibly created by the client
class.
Descriptor methods may use either, but descriptor state often makes it unnecessary to
use special naming conventions to avoid name collisions for descriptor data stored on
an instance. For example, the following descriptor attaches information to its own
instance, so it doesn¡¯t clash with that on the client class¡¯s instance:

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