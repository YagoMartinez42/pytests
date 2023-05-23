from pygame import *
import os

clock = time.Clock()
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
FPS = 60
y1 = 250
y2 = 250
x1 = 500
x2 = 100
os.chdir("C:/Users/alcob/Documents/Python/Pygame")
window = display.set_mode((700, 500))
display.set_caption("catch")
background = transform.scale(image.load("background.png"), (700, 500))
sprite1 = transform.scale(image.load("sprite1.png"), (100, 100))
sprite2 = transform.scale(image.load("sprite2.png"), (100, 100))
game = True
while game:
    clock.tick(FPS)
    window.blit(background,(0, 0))
    window.blit(sprite1,(x1, y1))
    window.blit(sprite2,(x2, y2))
    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= 10
    elif keys_pressed[K_DOWN] and y1 < 395:
        y1 += 10
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= 10
    elif keys_pressed[K_RIGHT] and x1 < 595:
        x1 += 10
    if keys_pressed[K_w] and y2 > 5:
        y2 -= 10
    elif keys_pressed[K_s] and y2 < 395:
        y2 += 10
    if keys_pressed[K_a] and x2 > 5:
        x2 -= 10
    elif keys_pressed[K_d] and x2 < 595:
        x2 += 10
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
