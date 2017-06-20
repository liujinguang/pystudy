#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月20日

@author: bob
In short, if a class defines or
inherits the following methods, they will be run automatically when an instance is used
in the context described by the comments to the right:
    def __getattr__(self, name):          # On undefined attribute fetch [obj.name]
    def __getattribute__(self, name):     # On all attribute fetch [obj.name]
    def __setattr__(self, name, value):   # On all attribute assignment [obj.name=value]
    def __delattr__(self, name):          # On all attribute deletion [del obj.name]
'''

class Catcher(object):
    def __getattr__(self, name):
        print('Get:', name)
        
    def __setattr__(self, name, value):
        print('Set:', name, value)

if __name__ == '__main__':
    x = Catcher()
    x.job
    x.pay
    x.pay = 99
    