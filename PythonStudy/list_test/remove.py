'''
Created on Jun 7, 2017

@author: bob
'''


if __name__ == '__main__':
    #remove dumplicated items from list
    l1 = ['b','c','d','b','c','a','a']
    
    print list(set(l1))
    print {}.fromkeys(l1)