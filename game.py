from easygame import *
import time

open_window('Panda simulator', 1620, 928)

mikox = 0
mikoy= 256
xdir = "0"
ydir = "0"
resx = 1620
resy = 928
resxdiv2 = resx/2
resydiv2 = resy/2

open_window('Panda simulator', resx, resy)

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
m = load_image("assets/character.png")


should_quit = False
while not should_quit:
    fill(0.45, 0.9, 1)
    draw_image(m, (mikox,mikoy))
    draw_image(main_background, (400, 400), rotation=0, scale=10, pixelated=True)


    if (mikoy > 256):
        mikoy -= (time_falling/9.81)
        time_falling += 1
    if not mikoy > 256:
        time_falling = 0
        ydir = "0"

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

    
    next_frame()
 
close_window()
close_window()
