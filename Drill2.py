from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

rect = True
centerx = 400
centery = 300

charLocx = 400
charLocy = 90
charSize = 30

angle = 270
r = 210


while True:
    while rect == True:
        while (charLocx < 800 - charSize):
            clear_canvas_now()
            grass.draw_now(400, 30)
            charLocx += 2
            character.draw_now(charLocx, charLocy)
            delay(0.01)
        while (charLocy < 600 - charSize):
            clear_canvas_now()
            grass.draw_now(400, 30)
            charLocy += 2
            character.draw_now(charLocx, charLocy)
            delay(0.01)
        while (charLocx > charSize):
            clear_canvas_now()
            grass.draw_now(400, 30)
            charLocx -= 2
            character.draw_now(charLocx, charLocy)
            delay(0.01)
        while (charLocy > 90):
            clear_canvas_now()
            grass.draw_now(400, 30)
            charLocy -= 2
            character.draw_now(charLocx, charLocy)
            delay(0.01)
        while (charLocx < 400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            charLocx += 2
            character.draw_now(charLocx, charLocy)
            delay(0.01)
        rect = False

    while (rect == False):
        clear_canvas_now()
        grass.draw_now(400, 30)
        charLocx = centerx + r * math.cos(math.radians(angle))
        charLocy = centery + r * math.sin(math.radians(angle))
        angle = (angle + 2) % 360
        character.draw_now(charLocx, charLocy)
        delay(0.01)
        if angle == 270: rect = True


delay(2)

close_canvas()

