#!/usr/bin/python3
import math
import time

from tkinter import *
from math import pi
from math import cos
from math import sin


class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="UPDATE", fg="red", command=self.animate
            )
        self.button.pack(side=LEFT)

        self.canvas = Canvas(master, width=900, height=700, borderwidth=0, highlightthickness=0, bg="black")
        #self.circ1 = self.canvas.create_oval(10, 10, 80, 80, outline="gray", fill="gray", width=2)
        #self.circ2 = self.canvas.create_oval(10, 20, 80, 90, outline="red", fill="gray", width=2)
        #self.circle=self.canvas.create_oval(50,50,80,80,outline="white",fill="blue")

        ###############John's fancy witchcraft ###################
        i = 0
        radius = 300
        bead_radius = 10
        stem_spacing = radius * pi * 2 / 56
        x_offset = radius + (stem_spacing * 4) + 50
        y_offset = 325
        #make the stem
        for i in range(0, 4):
            x = (x_offset - radius - stem_spacing * 4) + (stem_spacing * i)
            y = y_offset
            self.canvas.create_oval(x, y, x+(2*bead_radius),y+(2*bead_radius), fill="gray", width=2)

        #make the rest of the beads
        for i in range(4, 60):
            angle = (pi * 2 / 56 * (i - 4)) - pi
            x = x_offset + radius * cos(angle)
            y = y_offset + radius * sin(angle)
            self.canvas.create_oval(x, y, x+(2*bead_radius), y+(2*bead_radius), fill="gray", width=2)
        ##########################################################

        self.canvas.pack()

    def animate(self):
        self.canvas.move(self.circle,5,5)
        self.canvas.move(self.circ1,5,5)
        #self.canvas.after(100, self.animate)

def main(queue):
    animation = Tk()
    app = App(animation)
    while True:
        msg = queue.get()         # Read from the queue and do nothing
        if (msg == 'update'):
            animation.update_idletasks()
            animation.update()
            print("Updating")
        
