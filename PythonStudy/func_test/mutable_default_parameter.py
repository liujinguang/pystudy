#/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年5月30日

@author: bob
'''

#Many will mistakenly expect list1 to be equal to [10] and list3 to be equal to ['a'], thinking that the list 
#argument will be set to its default value of [] each time extendList is called.

#However, what actually happens is that the new default list is created only once when the function is defined, 
#and that same list is then used subsequently whenever extendList is invoked without a list argument being specified. 
#This is because expressions in default arguments are calculated when the function is defined, not when it’s called.

#list1 and list3 are therefore operating on the same default list, whereas list2 is operating on a separate 
#list that it created (by passing its own empty list as the value for the list parameter).
#


def function(data=[]):
    data.append(5)
    return data

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

if __name__ == '__main__':
    print dir(function)
    print(id(function()))
    print(id(function()))
    print(id(function()))
