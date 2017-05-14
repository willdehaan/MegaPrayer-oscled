# -*- coding: utf-8 -*-
"""
instantiate a process object
with a target function and 
arguments and call start() 
"""

import multiprocessing
from multiprocessing import Queue
import simulator
import OSCserver

def sim(queue):
    print("Starting Simulator...")
<<<<<<< HEAD
    simulator.main(queue)
=======
    #simulator.main()
    while True:
        msg = queue.get()         # Read from the queue and do nothing
        if (msg == 'update'):
            print("Updating")
            break
>>>>>>> d795ff7b0a8b3fbf5a367c1e3af45aad4b2c8ce3

def serve(queue):
    print("Starting OSC Server...")
    OSCserver.main(queue)


if __name__ == '__main__':
    queue = Queue() 
    p = multiprocessing.Process(target=sim, args=((queue),))
    q = multiprocessing.Process(target=serve, args=((queue),))
    p.start()
    q.start()

