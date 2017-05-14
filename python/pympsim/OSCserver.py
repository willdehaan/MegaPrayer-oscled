"""OSC server

This program listens for /beadf messages from MP
"""
import argparse
import math

from pythonosc import dispatcher as disp
from pythonosc import osc_server

my_queue = None

def print_bead(addr, args):
    #print(one, two, three, four, five)
    queue = args[0]
    queue.put('one')
    
<<<<<<< HEAD
def print_update(addr, args):
=======
#def print_update(addr, args, queue):
def print_update(addr, args):
    global my_queue
    #queue.put('update')
    print(args)
    #my_queue.put('update')
>>>>>>> d795ff7b0a8b3fbf5a367c1e3af45aad4b2c8ce3
    queue = args[0]
    queue.put('update')

def main(queue):
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
                        type=int, default=5005, help="The port to listen on")
    args = parser.parse_args()

    my_queue = queue
    dispatcher = disp.Dispatcher()
    #dispatcher.map("/beadf", print_bead, queue)
    dispatcher.map("/update", print_update, queue)
    #dispatcher.map("/update", print_update)

    server = osc_server.ThreadingOSCUDPServer(
            (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
