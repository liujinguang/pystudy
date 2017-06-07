'''
Created on Jun 7, 2017

@author: bob
'''

def binary_search(l, t):
    low, high = 0, len(l) - 1
    
    while low < high:
        
        mid = (low + high) / 2
        
        print low, mid, high
        
        if l[mid] > t:
            high = mid
        elif l[mid] < t:
            low = mid + 1
        else:
            return mid
        
    return low if l[low] == t else False

if __name__ == '__main__':
    l = [1, 4, 12, 45, 66, 99, 120, 444]
    print binary_search(l, 66)
