import pgzrun
import random

FONT_option = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2
CENTRE = (CENTRE_X, CENTRE_Y)
FINAL_LEVEL = 6
START_SPEED = 10

game_over = False
game_complete = False
current_level = star = Actor("star")
items = []
animations = []

def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("background", (0, 0))
    if game_over:
        display_message("GAME OVER", "Try again.")
    elif game_complete:
        display_message("YOU WON!", "Well done.")
    else:
      for item in items:
          item.draw()

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)


pgzrun.go()