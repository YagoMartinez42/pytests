from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class PlayerSprite(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys_pressed = key.get_pressed()
        if (keys_pressed[K_UP] or keys_pressed[K_w]) and self.rect.y > 5:
            self.rect.y -= self.speed
        elif (keys_pressed[K_DOWN] or keys_pressed[K_s]) and self.rect.y < (window.get_height() - 70):
            self.rect.y += self.speed
        if (keys_pressed[K_LEFT] or keys_pressed[K_a]) and self.rect.x > 5:
            self.rect.x -= self.speed
        elif (keys_pressed[K_RIGHT] or keys_pressed[K_d]) and self.rect.x < (window.get_width() - 70):
            self.rect.x += self.speed

class EnemySprite(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        direction = True
        if self.rect.x > 1200:
            direction = True
        elif self.rect.x < 800:
            direction = False
        if direction == False:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

def drawMaze():
    walls = []
    walls.append(Wall(119, 119, 0, 20, 700, 1500, 15))
    walls.append(Wall(119, 119, 0, 20, 20, 15, 690))
    walls.append(Wall(119, 119, 0, 20, 20, 800, 15))
    walls.append(Wall(119, 119, 0, 620, 20, 15, 500))
    walls.append(Wall(119, 119, 0, 310, 140, 15, 565))
    walls.append(Wall(119, 119, 0, 900, 140, 15, 565))
    return(walls)

mixer.init()
mixer.music.load('fight.mp3')
mixer.music.play()
window = display.set_mode((1280, 720))
display.set_caption("catch")
background =  transform.scale(image.load("background.jpg"), (1280, 720))
player1 = PlayerSprite("hero.png", 100, 100, 10)
monster1 = EnemySprite("cyborg.png", 900, 500, 2)
treasure = GameSprite("treasure.png", 200, 200, 10)
walls = drawMaze()

clock = time.Clock()
FPS = 60
y2 = 250
x2 = 100
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    window.blit(background,(0, 0))
    player1.update()
    monster1.update()
    player1.draw()
    monster1.draw()
    treasure.draw()
    for w in walls:
        w.draw_wall()
    
    display.update()
