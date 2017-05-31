'''
Created on May 27, 2017

@author: bob
'''

# class Descriptor:
#     "docstring goes here"
#     def __get__(self, instance, owner): ... # Return attr value
#     def __set__(self, instance, value): ... # Return nothing (None)
#     def __delete__(self, instance): ... # Return nothing (None)

class Descriptor(object):
    def __get__(self, instance, owner):
        print(self, instance, owner)
        
        
class Subject(object):
    attr = Descriptor()

if __name__ == '__main__':
    X = Subject()
    
    X.attr