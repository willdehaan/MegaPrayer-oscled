"""OSC server

This program listens for /beadf messages from MP
"""
import argparse
import math

from pythonosc import dispatcher as disp
from pythonosc import osc_server


def print_volume_handler(unused_addr, args, volume):
    print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(unused_addr, args, volume):
    try:
        print("[{0}] ~ {1}".format(args[0], args[1](volume)))
    except ValueError: pass

def print_bead(unused_addr, args, q):
    #print(one, two, three, four, five)
    for i in range(0, len(args)):
        print(args[i])
    #queue.put('one')
    
def print_update(addr, args, queue):
    queue.put('update')

def main(queue):
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
                        type=int, default=5005, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = disp.Dispatcher()
    #dispatcher.map("/beadf", print_bead, queue)
    dispatcher.map("/update", print_update, queue)

    server = osc_server.ThreadingOSCUDPServer(
            (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
