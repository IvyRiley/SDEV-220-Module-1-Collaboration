#Use multiprocessing to create three separate processes. 
# Make each one wait a random number of seconds between zero and one, 
# print the current time, and then exit.

import multiprocessing
import os
import random
import time
import subprocess

def func_process(what):
    randomeTime = random.randrange(0,1)
    time.sleep(randomeTime)
    print("Process %s says: %s" % (os.getpid(), what + " took " + str(randomeTime) + " seconds"))
    
if __name__ == "__main__":
    for n in range(3):
        p = multiprocessing.Process(target=func_process,
        args=("I'm function %s" % (n + 1),))
        p.start()

