'''
Created on Jun 19, 2017

@author: bob
'''

#Python automatically maps instance method calls to class method
#functions as follows. Method calls made through an instance, like this:
#    instance.method(args...)
#are automatically translated to class method function calls of this form:
#    class.method(instance, args...)


class NextClass(object):
    def printer(self, text):
        self.message = text
        print(self.message)

if __name__ == '__main__':
    x = NextClass()
    x.printer("instance call")
    print x.message
    
    NextClass.printer(x, "class call")
    print x.message