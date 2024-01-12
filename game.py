from easygame import *
import time

open_window('Panda simulator', 1620, 928)

mikox = 0
mikoy= 256
xdir = "0"
ydir = "0"

def mikoMovement():
    global mikox, mikoy
    if (xdir == "+"):
        mikox += 1
    if (xdir == "-"):
        mikox -= 1
    if (ydir == "+"):
        mikoy += 5
    if (ydir == "-"):
        mikoy -= 1

should_quit = False
while not should_quit:
    fill(0.45, 0.9, 1)
    m = load_image("assets/New_Piskel.png")
    draw_image(m, (mikox,mikoy))

    for event in poll_events():
        if type(event) is KeyDownEvent:
            if (event.key == 'W'):
                ydir = "+"
            if (event.key == 'S'):
                ydir = "-"
            if (event.key == 'A'):
                xdir = "-"
            if (event.key == 'D'):
                xdir = "+"
        if type(event) is KeyUpEvent:
            if (event.key == 'W'):
                ydir = "0"
            if (event.key == 'S'):
                ydir = "0"
            if (event.key == 'A'):
                xdir = "0"
            if (event.key == 'D'):
                xdir = "0"
        if type(event) is CloseEvent:
            should_quit = True
        ##jak to ide
        
    mikoMovement()
    if (mikoy > 256):
        mikoy -= (time_falling/9.81)
        time_falling += 1
    if not mikoy > 256:
        time_falling = 0
    
    next_frame()
 
close_window()
close_window()
