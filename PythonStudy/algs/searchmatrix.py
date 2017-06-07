'''
Created on Jun 7, 2017

@author: bob
'''

def get_value(l, r, c):
    return l[r][c]

def find(l, x):
    m = len(l) - 1
    n = len(l[0]) - 1
    
    r = 0
    c = n
    
    while c >= 0 and r <= m:
        value = get_value(l, r, c)
        if value == x:
            return True
        elif value > x:
            c 

if __name__ == '__main__':
    pass