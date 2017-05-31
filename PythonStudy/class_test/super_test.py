#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月30日

@author: bob
'''

class Base(object):
    def __init__(self):
        print "Base created"
        
class ChildA(Base):
    def __init__(self):
        Base.__init__(self)
        
class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

if __name__ == '__main__':
    print ChildA()
    print ChildB()