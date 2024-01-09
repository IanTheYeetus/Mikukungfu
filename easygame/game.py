from easygame import *

open_window('Panda simulator', 800, 600)


should_quit = False
while not should_quit:
    fill(0.3, 0.65, 1)

    for event in poll_events():

        if type(event) is CloseEvent:
            should_quit = True
    draw_text("SuShi", "Arial", 255)
    next_frame()
 
close_window()