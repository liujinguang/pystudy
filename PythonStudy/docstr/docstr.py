#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月19日

@author: bob

I am: docstr.__doc__
'''

# "I am: docstr.__doc__"

def func(args):
    "I am: docstr.func.__doc__"
    pass
class spam:
    "I am: spam.__doc__ or docstr.spam.__doc__"
    def method(self, arg):
        "I am: spam.method.__doc__ or self.method.__doc__"
        pass

if __name__ == '__main__':
    pass