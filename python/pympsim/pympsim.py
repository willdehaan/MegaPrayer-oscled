# -*- coding: utf-8 -*-
"""
instantiate a process object
with a target function and 
arguments and call start() 
"""

import multiprocessing
import simulator
import OSCserver

def sim():
    print("Starting Simulator...")
    simulator.main()

def serve():
    print("Starting OSC Server...")
    OSCserver.main()

if __name__ == '__main__':
    p = multiprocessing.Process(target=sim)
    q = multiprocessing.Process(target=serve)
    p.start()
    q.start()
    print(OSCserver.update)
    while True:
        if (OSCserver.update == 1):
            print('time to update!')
            OSCserver.update = 0
