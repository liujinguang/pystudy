#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年6月1日

@author: bob
'''

class TestClass(object):
    val1 = 100
    
    def __init__(self):
        self.val2 = 200
        
    def fcn(self, val=400):
        val3 = 300
        self.val4 = val
        self.val5 = 500

if __name__ == '__main__':
#     inst = TestClass()  
#        
#     print TestClass.val1  
#     print inst.val1  
#     print inst.val2  
#     inst.fcn()
# #     print inst.val3  
#     print inst.val4      
#     print inst.val5      
    
    inst1 = TestClass()  
    inst2 = TestClass()  
       
    print TestClass.val1 # 100  
    print inst1.val1     # 100  
    print "*" * 20
    inst1.val1 = 1000      
    print inst1.val1     # 1000  
    print TestClass.val1 # 100  
    
    print "*" * 20
    TestClass.val1 =2000   
    print inst1.val1     # 1000  
    print TestClass.val1 # 2000  
      
    print inst2.val1     # 2000       
    
    print "*" * 20
    inst3 = TestClass()    
    print inst3.val1     # 2000  