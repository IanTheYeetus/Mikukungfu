from easygame import *

open_window('Epic Gamer Fortnite Mikukáš Adventure', 1470, 956)
 
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
    ###
 
    # Pokračuj na ďalšiu snímku (a všetko opať prekresli)
    next_frame()
 
close_window()
