#!/usr/bin/python3
import math
import time

from tkinter import *


class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="UPDATE", fg="red", command=self.animate
            )
        self.button.pack(side=LEFT)

        self.canvas = Canvas(master, width=700, height=700, borderwidth=0, highlightthickness=0, bg="black")
        self.circ1 = self.canvas.create_oval(10, 10, 80, 80, outline="gray", 
            fill="gray", width=2)
        self.circ2 = self.canvas.create_oval(10, 20, 80, 90, outline="red", 
            fill="gray", width=2)
        self.circle=self.canvas.create_oval(50,50,80,80,outline="white",fill="blue")

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
        
