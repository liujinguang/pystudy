'''
Created on Jun 7, 2017

@author: bob
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
def cross_node(l1, l2):
    length1, length2 = 0, 0
    
    l1_tmp, l2_tmp = l1, l2
    
    while l1_tmp.next:
        l1_tmp = l1_tmp.next
        length1 += 1
        
    while l2_tmp.next:
        l2_tmp = l2_tmp.next
        length2 += 1
        
        
    if length1 > length2:
        for _ in xrange(length1 - length2):
            l1 = l1.next
    else:
        for _ in xrange(length2 - length1):
            l2 = l2.next
            
    while l1 and l2:
        if l1.next == l2.next:
            return l1.next
        else:
            l1 = l1.next
            l2 = l2.next
            

if __name__ == '__main__':
    pass