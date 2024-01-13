from easygame import *
from funkcie import *
from perlin_noise import PerlinNoise
import random

bodiky = 0
seed = 1
noise = PerlinNoise(octaves=1000, seed=seed)

strcondF = "(mikoy < 64 and mikoy > 0)"
strcondC = "False"
strcondDumpling = "False"

main_background = load_image("assets/General_texture.png")
main_block = load_image("assets/Object_texture.png")
ArrayBackrounds = ["assets/General_texture.png", "assets/Background_texture2.png", "assets/Background_texture3.png", "assets/Background_texture4.png", "assets/macker.png"]
ArrayBlocks = ["assets/Object_texture.png", "assets/Object_texture_2.png", "assets/Object_texture3.png", "assets/Object_texture4.png"]


class dumpling:
    def __init__(self, x, y) -> None:
        global strcondDumpling
        self.x = x
        self.y = y
        self.obj = draw_image(load_image("assets/dump.png"), (x, y), pixelated=True, anchor=(0,0))
        strcondDumpling += " or (mikox < " + str(x+5) + " and mikox > " + str(x-5) + " and mikoy < " + str(y+5) + " and mikoy > " + str(y-5) + ")"

class block:
    def __init__(self, x, y) -> None:
        global strcondF
        global strcondC
        self.x = x
        self.y = y
        self.obj = draw_image(main_block, (x, y), pixelated=True, anchor=(0,0))
        strcondF += " or ((mikoy < " + str(y + 64 + 5) + " and mikoy > " + str(y + 64 -15) + ") and mikox > " + str(x-32) + " and mikox <" + str(x + 32) + ")"
        strcondC += " or ((mikoy < " + str(y+64-5) + " and mikoy > " + str(y-59) + ") and mikox > " + str(x-32) + " and mikox <" + str(x + 32) + ")"
        if ((noise([self.x/resx, self.y/resy])) > 0.2):
            dumpling(x+16, y+64)
            
        

def makeNBlocks(n, start_x=0, start_y=0, dir=0):
    """_summary_

    Args:
        n (int): number of blocks in a row
        start_x (int, optional): from where to start drawing X
        start_y (int, optional): from when to start drawing Y
        dir (int 0, 1): horizontal or vertical. Horizontal by default
    """
    if (dir == 0):
        i = 0
        while i < n*64:
            block(start_x + (i), start_y)
            i += 64
    elif (dir == 1):
        i = 0
        while i < n*64:
            block(start_x, start_y + (i))
            i += 64

mikox = 0
mikoy= 64
xdir = "0"
ydir = "0"
resx = 1792
resy = 896
resxdiv2 = resx/2
resydiv2 = resy/2
time_falling = 0

open_window('Panda simulator', resx, resy)

rnd = random.randint(5, 10)
a1 = []
a2 = []
a3 = []
a4 = []



def genLevel():
    global seed, strcondF, strcondC, strcondDumpling, main_background, main_block, ArrayBackrounds, ArrayBlocks
    strcondF = "(mikoy < 64 and mikoy > 0)"
    strcondC = "False"
    strcondDumpling = "False"
    seed += 1
    mn = 0
    global a1, a2, a3, a4, rnd
    rnd = random.randint(5, 10)
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    main_block = load_image(ArrayBlocks[random.randint(0,3)])
    if bodiky < 28:
        main_background = load_image(ArrayBackrounds[random.randint(0,3)])
    elif bodiky >= 28:
        main_background = load_image(ArrayBackrounds[4])

    while mn < rnd:
        a1.append(random.randint(2, 9))
        a4.append(random.randint(0, 1))
        a2.append(random.randint(0, 14))
        a3.append(random.randint(1, random.randint(1, 7)))
        mn += 1

def mikoMovement():
    global mikox, mikoy
    if (xdir == "+"):
        mikox += 3
    if (xdir == "-"):
        mikox -= 3
    if (ydir == "+"):
        mikoy += 6.5
    if (ydir == "-"):
        mikoy -= 1

m = load_image("assets/character.png")
should_quit = False

genLevel()

while not should_quit:
    draw_image(main_background, (0, 0), anchor=(0, 0), rotation=0, scale=10, pixelated=True)

    strcondF = "(mikoy < 64 and mikoy > 0)"
    strcondC = "False"
    strcondDumpling = "False"
    
    yi = 0
    while yi < rnd:
        makeNBlocks(a1[yi], a2[yi]*128, a3[yi]*128, a4[yi])
        yi += 1
    floortiling = 0
    while floortiling < resx:
        draw_image(main_block, (floortiling, 0), pixelated=True, anchor=(0,0))
        floortiling += 64

    draw_image(m, position=(mikox,mikoy), anchor=(32, 0))
    ##draw_text(str(noise(mikox/resx)), "arial", 67)
    conditionFloor = eval(strcondF)
    conditionCeiling = eval(strcondC)

    if not conditionFloor:
        mikoy -= ((time_falling/100)*9.81)
        time_falling += 1
    if conditionCeiling:
        ydir = "-"
        xdir = "0"
    if conditionFloor:
        time_falling = 0
        ydir = "0"


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
                print((strcondDumpling))
            if (event.key == 'O'):
                bodiky -= 1
                genLevel()
            if (event.key == 'C'):
                bodiky += 1
        if type(event) is CloseEvent:
            should_quit = True

    if eval(strcondDumpling):
        bodiky += 3
        genLevel()
        
    mikoMovement()
    draw_text(text="Body: "+str(bodiky), font="times_new_roman", size=60, position=(resx-340, resy-80), anchor=("left", "bottom"), color = (13/255, 234/255, 255/255, 1), bold=True, ui=True)
    
    next_frame()
 
close_window()