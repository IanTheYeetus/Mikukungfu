from easygame import *

class block:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.obj = draw_image(load_image("assets/Object_texture.png"), (x, y), pixelated=True)

def makeNBlocks(n, start_x=0, start_y=0):
    i = 0
    while i < n*64:
        block(start_x + (i), start_y)
        i += 64