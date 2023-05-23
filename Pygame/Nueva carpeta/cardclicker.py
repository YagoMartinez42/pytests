import pygame
import random

'''clase de rectángulo'''
class Area():
   def __init__(self, x=0, y=0, width=10, height=10, color=None):
       self.rect = pygame.Rect(x, y, width, height) #rectángulo
       self.fill_color = color

   def color(self, new_color):
       self.fill_color = new_color
   def fill(self):
       pygame.draw.rect(mw, self.fill_color, self.rect)
   def outline(self, frame_color, thickness): #delimita un rectángulo existente
       pygame.draw.rect(mw, frame_color, self.rect, thickness)    

'''etiqueta de clase'''
class Label(Area):
   def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
       self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
   def draw(self, shift_x=0, shift_y=0):
       self.fill()
       mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
LIGHT_GREEN = (48, 255, 128)
RED = (255, 0, 0)
cards = []
num_cards = 4
x = 70
points = 0

pygame.init()
'''crear ventana de juego'''
back = (200, 255, 255) #color de fondo
mw = pygame.display.set_mode((500, 500)) #ventana principal
mw.fill(back)
clock = pygame.time.Clock()
changeStart = pygame.time.get_ticks()

for i in range(num_cards):
   new_card = Label(x, 170, 70, 100, YELLOW)
   new_card.outline(BLUE, 10)
   new_card.set_text("", 26)
   cards.append(new_card)
   x = x + 100

while True:
   change = pygame.time.get_ticks()
   mw.fill(back)
   if change - changeStart > 1000:
      changeStart = pygame.time.get_ticks()
      target = random.randint(0, 3)
      for card in cards:
         card.set_text("", 1)
      cards[target].set_text("Click", 26)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
         if cards[target].rect.collidepoint(event.pos):
            points += 1
            cards[target].color(LIGHT_GREEN)
         else:
            points -= 1
            cards[target].color(RED)
   for card in cards:
       card.draw(10, 30)
   pygame.display.update()
   clock.tick(40)
