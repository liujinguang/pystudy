#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Jun 27, 2017

@author: bob
'''

class CardHolder(object):
    acctlen = 8
    retireage = 59.5
    
    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr
        
    def __getattribute__(self, name):
        superget = object.__getattribute__
        if name == 'acct':
            return superget(self, 'acct')[:-3] + '***'
        elif name == 'remain':
            return superget(self, 'retireage') - superget(self, 'age')
        else:
            return superget(self, name)
        
    def __setattr__(self, name, value):
        if name == 'name':
            value = value.lower().replace(' ', '_')
        elif name == 'acct':
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invalid acct number')
        elif name == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        
        self.__dict__[name] = value

if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr)
#     print "aa", "bb", sep=' '
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr)
    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    print(sue.acct, sue.name, sue.age, sue.remain, sue.addr)
    
    try:
        sue.age = 200
    except:
        print('Bad age for Sue')
        
    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")
        
    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')    