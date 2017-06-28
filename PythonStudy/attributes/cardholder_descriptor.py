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
        
    class Name(object):
        def __get__(self, instance, owner):
            return self.name 
        
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value
            
    name = Name()
    
    class Age(object):
        def __get__(self, instance, owner):
            return self.age
        
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                self.age = value
    
    age = Age()
    
    class Acct(object):
        def __get__(self, instance, owner):
            return self.acct[:-3] + "***"
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:
                raise TypeError('invalid acct number')
            else:
                self.acct = value
                
    acct = Acct()
    
    class Remain(object):
        def __get__(self, instance, owner):
            return instance.retireage - instance.age
        
        def __set__(self):
            raise TypeError('cannot set remain')
    remain = Remain()

if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr)    
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