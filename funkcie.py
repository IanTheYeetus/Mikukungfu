from easygame import *


# class block:
#     def __init__(self, x, y, strcondF) -> None:
#         self.x = x
#         self.y = y
#         self.obj = draw_image(load_image("assets/Object_texture.png"), (x, y), pixelated=True)
#         strcondF += " or ((mikoy < " + str(y + 64 + 5) + " and mikoy > " + str(y + 64 -5) + ") and mikox > " + str(x) + " and mikox <" + str(x + 64) + ")"

# def makeNBlocks(n, start_x=0, start_y=0, cond=""):
#     i = 0
#     while i < n*64:
#         block(start_x + (i), start_y, cond)
#         i += 64

## or ((mikoy < 134 + 5 and mikoy > 134-5) and mikox > 100 and mikox < 164))