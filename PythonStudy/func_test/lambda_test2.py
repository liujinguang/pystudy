'''
Created on Jun 1, 2017

@author: bob
'''

if __name__ == '__main__':
    print map(lambda x: x* x, range(10))
    print reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
    
    list1 = [3,5,-4,-1,0,-2,-6]
    print sorted(list1, key=lambda x: abs(x))