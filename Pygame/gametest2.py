import pygame

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

pygame.init()
mw = pygame.display.set_mode((1280, 720))
mw.fill((168,168,168))
clock = pygame.time.Clock()
cosilla1 = Area (60,60, 100, 200, (0,0,0))
cosilla2 = Area (360,60, 100, 200, (0,0,0))
textimage = pygame.font.SysFont('verdana', 30)
textimage = textimage.render("Tarjeta 1", True, (255, 255, 255))


while True:
   cosilla1.fill()
   cosilla2.fill()
   mw.blit(textimage, (cosilla1.rect.x + 10, cosilla1.rect.y + 90))
   pygame.display.update()
   clock.tick(40) 
