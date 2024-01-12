from easygame import *
import time


mikox = 0
mikoy= 0
xdir = "0"
ydir = "0"
resx = 1800
resy = 975
resxdiv2 = resx/2
resydiv2 = resy/2
time_falling = 0

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
main_background = load_image("assets/General_texture.png")


should_quit = False
while not should_quit:
    fill(0.45, 0.9, 1)
    draw_image(main_background, (0, 0), anchor=(0, 0), rotation=0, scale=10, pixelated=True)
    p1 = draw_image(load_image("assets/Object_texture.png"), (100, 100), pixelated=True)
    draw_image(m, (mikox,mikoy))
    draw_text(str(time_falling/150), "arial", 67)
    conditionFloor = ((mikoy < 5 and mikoy > -5) or ((mikoy < 110 + 5 and mikoy > 110-5) and mikox > 100 and mikox < 600) or )

    if not conditionFloor:
        mikoy -= ((time_falling/100)*9.81)
        time_falling += 1
    if conditionFloor:
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
