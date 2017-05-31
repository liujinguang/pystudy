'''
Created on May 16, 2017

@author: bob
'''

import subprocess

if __name__ == '__main__':
    aa = subprocess.call(["ls", "-wwwl"])
#     print subprocess.CalledProcessError.returncode
    print "aa=" + str(aa)