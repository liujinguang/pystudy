#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月29日

@author: bob

Qualified attribute names refer to attributes of specific objects and obey the rules for
modules and classes. For class and instance objects, the reference rules are augmented
to include the inheritance search procedure:

Assignment (object.X = value)
    Creates or alters the attribute name X in the namespace of the object being qualified,
    and none other. Inheritance-tree climbing happens only on attribute reference,
    not on attribute assignment.
Reference (object.X)
    For class-based objects, searches for the attribute name X in object, then in all
    accessible classes above it, using the inheritance search procedure. For nonclass
    objects such as modules, fetches X from object directly.
'''

class Person(object):
    name = "aaaa"
    
class Animal(object):
    name = []

if __name__ == '__main__':
    p1 = Person()
    p2 = Person()
    p1.name = "BBB"
    print p1.name
    print p2.name
    
    a1 = Animal()
    a2 = Animal()
    a1.name.append("hello")
    a2.name.append("world")
    
    print a1.name
    print a2.name
    