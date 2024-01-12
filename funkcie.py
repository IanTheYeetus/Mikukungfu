from easygame import *

class block:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.obj = draw_image(load_image("assets/Object_texture.png"), (x, y), pixelated=True)