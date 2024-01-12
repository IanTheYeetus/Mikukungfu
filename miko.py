from easygame import *
import math

res_x = 1470
res_y = 956

texture = load_image("assets/General_texture.png")
character = load_image("assets/character.png")

open_window('Epic Gamer Fortnite Mikukáš Adventure', res_x, res_y)
 
# Začni vykreslovať snímky v cykle (v predvolenej rýchlosti 60fps)
should_quit = False
while not should_quit:
    fill(0,0,0)
    # Načítaj udalosti pre aktuálnu snímku
    for event in poll_events():
        # Napríklad ak hráč spustí CloseEvent
        # prestaň ďalej vykreslovať snímky a zatvor okno 
        if type(event) is CloseEvent:
            should_quit = True

    
    draw_text("Fortnite", 'Times New Roman', 50, (200, 200))
    draw_image(character, (res_x/2, res_y/2), None, 0, 3)
    draw_image(texture, (res_x/2, res_y/2), None, 0, 5, 5, 5)
    ###
 
    # Pokračuj na ďalšiu snímku (a všetko opať prekresli)
    next_frame()
 
close_window()
