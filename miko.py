from easygame import *
import math

res_x = 1470
res_y = 956

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
    ###
    # Tu patrí logika hry, ktorá na obrazovku niečo vykreslí
    
    draw_text("Fortnite", 'Times New Roman', 50, (200, 200))
    test_image = load_image("General_texture.png")
    draw_image(test_image, (res_x/2, res_y/2), None, 0, 1, math.ceil(res_x/255), math.ceil(res_y/255))
    ###
 
    # Pokračuj na ďalšiu snímku (a všetko opať prekresli)
    next_frame()
 
close_window()
