'''
Created on Jun 7, 2017

@author: bob
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    """
    def swapPairs(self, head):
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next

if __name__ == '__main__':
    pass