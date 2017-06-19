'''
Created on May 27, 2017

@author: bob

Normally, attributes are simply names for objects; a person’s name attribute, for example, 
might be a simple string, fetched and set with basic attribute syntax:
    person.name # Fetch attribute value
    person.name = value # Change attribute value
In most cases, the attribute lives in the object itself, or is inherited from a class from
which it derives. That basic model suffices for most programs you will write in your
Python career.
Sometimes, though, more flexibility is required. Suppose you’ve written a program to
use a name attribute directly, but then your requirements change—for example, you
decide that names should be validated with logic when set or mutated in some way
when fetched. It’s straightforward to code methods to manage access to the attribute’s
value (valid and transform are abstract here):

However, this also requires changing all the places where names are used in the entire
program—a possibly nontrivial task. Moreover, this approach requires the program to
be aware of how values are exported: as simple names or called methods. If you begin
with a method-based interface to data, clients are immune to changes; if you do not,
they can become problematic.
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