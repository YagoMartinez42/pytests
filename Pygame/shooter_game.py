# ¡Crea tu propio juego de disparos!

from pygame import *
from random import randint

# clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.size_x = size_x
        self.size_y = size_y

        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # método que dibuja al personaje en la ventana
    def putPic(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# clase del jugador principal
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
    def update(self):
        keys_pressed = key.get_pressed()
        if (keys_pressed[K_LEFT] or keys_pressed[K_a]) and self.rect.x > 5:
            self.rect.x -= self.speed
        elif (keys_pressed[K_RIGHT] or keys_pressed[K_d]) and self.rect.x < (window.get_width() - 105):
            self.rect.x += self.speed
    def fire(self, bullets):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE]:
            bullet = Bullet("bullet.png", 0, 0, 3, 15, 15)
            bullet.reset(player1)
            bullets.add(bullet)
        return (bullets)

# clase del enemigo
class Enemy(GameSprite):
    def __init__(self, enemy_image, enemy_x, enemy_y, size_x, size_y, enemy_speed):
        super().__init__(enemy_image, enemy_x, enemy_y, size_x, size_y, enemy_speed)
    def reset(self):
        self.rect.y = 0
        self.rect.x = randint(0, 600)
    def update(self):
        global loses
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.reset()
            loses += 1

# clase del proyectil
class Bullet(GameSprite):
    def __init__(self, bullet_image, bullet_x, bullet_y, size_x, size_y, bullet_speed):
        super().__init__(bullet_image, bullet_x, bullet_y, size_x, size_y, bullet_speed)
    def reset(self, player):
        self.rect.x = player.rect.x + player.size_x / 2
        self.rect.y = player.rect.y
    def update(self):
        global wins
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
        if sprite.groupcollide(bullets, enemies, False, False):
            self.kill()
            wins += 1
    
mixer.init()
font.init()
mixer.music.load('fight.mp3')
mixer.music.play()
window = display.set_mode((700, 500))
display.set_caption("Galaxy Invaders")
background =  transform.scale(image.load("galaxy.jpg"), (700, 500))
player1 = Player("rocket.png", 350, 350, 100, 147, 10)
enemies = sprite.Group()
for e in range (5):
    e = Enemy("ufo.png", randint(0, 600), randint(0, 60), 100, 51, randint(1, 3))
    enemies.add(e)
bullets = sprite.Group()
clock = time.Clock()
FPS = 60
loses = 0
wins = 0
font2 = font.SysFont('Arial', 30, False, False)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    window.blit(background,(0, 0))
    player1.update()
    player1.putPic()
    bullets.update()
    bullets = player1.fire(bullets)
    enemies.draw(window)
    enemies.update()
    bullets.draw(window)
    text_lose = font2.render("Fallados: " + str(loses), True, (255, 255, 255))
    window.blit(text_lose, (20, 45))
    text_win = font2.render("Destruidos: " + str(wins), True, (255, 255, 255))
    window.blit(text_win, (20, 20))
    if loses >= 3 or sprite.spritecollide(player1, enemies, False):
        game = False
    if wins >= 10:
        game = False
    display.update()
text_gameover = font2.render("GAME OVER", True, (255, 255, 0))
window.blit(text_gameover, (280, 250))
display.update()


