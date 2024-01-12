from easygame import *
from funkcie import *
import time

strcondF = "(mikoy < 5 and mikoy > -5)"
strcondC = "False"

class block:
    def __init__(self, x, y) -> None:
        global strcondF
        global strcondC
        self.x = x
        self.y = y
        self.obj = draw_image(load_image("assets/Object_texture.png"), (x, y), pixelated=True, anchor=(0,0))
        strcondF += " or ((mikoy < " + str(y + 64 + 5) + " and mikoy > " + str(y + 64 -5) + ") and mikox > " + str(x) + " and mikox <" + str(x + 64) + ")"
        strcondC += " or ((mikoy < " + str(y-64+5) + " and mikoy > " + str(y-64-5) + ") and mikox > " + str(x) + " and mikox <" + str(x + 64) + ")"
def makeNBlocks(n, start_x=0, start_y=0):
    """_summary_

    Args:
        n (int): number of blocks in a row
        start_x (int, optional): from where to start drawing X
        start_y (int, optional): from when to start drawing Y
    """
    i = 0
    while i < n*64:
        block(start_x + (i), start_y)
        i += 64

mikox = 0
mikoy= 0
xdir = "0"
ydir = "0"
resx = 1800
resy = 900
resxdiv2 = resx/2
resydiv2 = resy/2
time_falling = 0

open_window('Panda simulator', resx, resy)

##strcondF = ((mikoy < 5 and mikoy > -5) or ((mikoy < 134 + 5 and mikoy > 134-5) and mikox > 100 and mikox < 164))


def mikoMovement():
    global mikox, mikoy
    if (xdir == "+"):
        mikox += 3
    if (xdir == "-"):
        mikox -= 3
    if (ydir == "+"):
        mikoy += 5
    if (ydir == "-"):
        mikoy -= 1
m = load_image("assets/character.png")
main_background = load_image("assets/General_texture.png")
should_quit = False
while not should_quit:
    ##fill(0.45, 0.9, 1)
    draw_image(main_background, (0, 0), anchor=(0, 0), rotation=0, scale=10, pixelated=True)

    strcondF = "(mikoy < 5 and mikoy > -5)"
    strcondC = "False"
    
    makeNBlocks(5, 100, 150)

    draw_image(m, position=(mikox,mikoy))
    draw_text(str(time_falling/150), "arial", 67)
    conditionFloor = eval(strcondF)
    conditionCeiling = eval(strcondC)

    if not conditionFloor:
        mikoy -= ((time_falling/100)*9.81)
        time_falling += 1
    if conditionFloor:
        time_falling = 0
        ydir = "0"
    if conditionCeiling:
        ydir = "-"

    for event in poll_events():
        if type(event) is KeyDownEvent:
            if (event.key == 'W'):
                ydir = "+"
            if (event.key == 'A'):
                xdir = "-"
            if (event.key == 'D'):
                xdir = "+"
        if type(event) is KeyUpEvent:
            if (event.key == 'A'):
                xdir = "0"
            if (event.key == 'D'):
                xdir = "0"
            if (event.key == 'B'):
                print(str(strcondF))
        if type(event) is CloseEvent:
            should_quit = True
        ##jak to ide
        
    mikoMovement()

    
    next_frame()
 
close_window()
