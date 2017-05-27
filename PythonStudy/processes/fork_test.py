'''
Created on May 13, 2017

@author: bob
'''

import os

if __name__ == '__main__':
    ret = os.fork()
    if ret == 0:
        os.execv("/bin/ls", ["-l", "/etc/network"])
    else:
        os.wait()