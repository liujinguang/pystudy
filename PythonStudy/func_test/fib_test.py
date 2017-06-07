'''
Created on Jun 7, 2017

@author: bob
'''

def memo(func):
    cache = {}
    
    def wrap(*args):
        cache[args] = func(*args)
#         print cache
        return cache[args]
    
    return wrap

@memo
def fib1(n):
    if (n < 2):
        return 1
    return fib1(n-1) + fib1(n-2)

def fib2(n):
    a, b = 0, 1
    
    for _ in xrange(n):
        a, b = b, a+b
        
    return b

if __name__ == '__main__':
    fib = lambda n: n if n <= 2 else fib(n-1) + fib(n-2)
    
    print fib(10)
    print fib2(10)
    
    print fib1(10)