'''
Created on May 31, 2017

@author: bob
'''

import threading
import time
import random

n = 0
lock = threading.Lock()
def foo():
    global n
    with lock:
        n += 1

if __name__ == '__main__':
    threads = []
    
    for i in range(1000):
        t = threading.Thread(target=foo)
        threads.append(t)
        
    for t in threads:
        t.start()
        
    for t in threads:
        t.join()
        
    print n