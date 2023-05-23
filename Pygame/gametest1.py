import pygame
from random import randint

pygame.init()

lightBlue = (128, 192, 255)
lilac = (192, 96, 255)
yellow = (255, 215, 0)
window = pygame.display.set_mode((500, 500))
rectangulo = pygame.Rect(190, 230, 120, 40)
font1 = pygame.font.Font(None, 20)
question = font1.render('Hola mundo', True, yellow)

class TextArea():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pygame.Rect(x, y, width, height)
      self.fill_color = color
      self.text_list = ['¿Cuál es la fórmula del área de un círculo?',
                        '¿Cual es la capital de Turquía?',
                        '¿Con cuántos años murió la reina Isabel II de Inglaterra?',
                        'En qué año empezó la Primera Guerra Mundial']

  def set_text(self, text, fsize=24, text_color=yellow):
      self.text = text
      self.image = pygame.font.Font(None, fsize).render(text, True, text_color)

  def draw(self, shift_x=0, shift_y=0):
      pygame.draw.rect(window, self.fill_color, self.rect)
      window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

  def get_from_list (self):
      idx = randint (0, len(self.text_list))


window.fill(lightBlue)
#pygame.draw.rect(window, lilac, rectangulo)
#window.blit(question, (210, 250))
cuadrito = TextArea(190, 230, 120, 40, lilac)
cuadrito.set_text('Hola mundo') 
cuadrito.draw(10, 16)
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            print('adios')
pygame.display.update()

