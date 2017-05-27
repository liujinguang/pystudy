'''
Created on May 26, 2017

@author: bob
'''

# class Foo(object):
#     bar = True
#     
# class FooChild(Foo):
#     pass

def echo_bar(self):
    print(self.bar)
    
def echo_bar_more(self):
    print('yet another method')

if __name__ == '__main__':
    Foo = type('Foo', (), {'bar' : True})
    
    print(Foo)
    print(Foo.bar)
    
    f = Foo()
    print(f)
    print(f.bar)
    
    FooChild = type('FooChild', (Foo, ), {'echo_bar' : echo_bar})
    print(FooChild)
    
    print(hasattr(FooChild, 'echo_bar'))
    
    FooChild.echo_bar_more = echo_bar_more
    print(hasattr(FooChild, 'echo_bar_more'))