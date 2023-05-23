import pygame
pygame.init()

#flag del final del juego
game_over = False
#una clase de un proyecto anterior
class Area():
   def __init__(self, x = 0, y = 0, width = 10, height = 10, color = None):
       self.rect = pygame.Rect(x, y, width, height)
       self.fill_color = back
       if color:
           self.fill_color = color

   def color(self, new_color):
       self.fill_color = new_color

   def fill(self):
       pygame.draw.rect(mw, self.fill_color, self.rect)

   def collidepoint(self, x, y):
       return self.rect.collidepoint(x, y)       

   def colliderect(self, rect):
       return self.rect.colliderect(rect)

#clase para objetos de imagen
class Picture(Area):
   def __init__(self, filename, x=0, y=0, width=10, height=10):
       Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
       self.image = pygame.image.load(filename)
      
   def draw(self):
       mw.blit(self.image, (self.rect.x, self.rect.y))

back = (0, 32, 64) #color de fondo
mw = pygame.display.set_mode((500, 500)) #ventana principal
mw.fill(back)
clock = pygame.time.Clock()

#Coordenadas de la plataforma
racket_x = 200
racket_y = 330

#creando una pelota y la plataforma   
ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', racket_x, racket_y, 100, 30)

#creando enemigos
start_x = 5 #coordenadas de la creación del primer monstruo
start_y = 5
count = 9 #número de monstruos en la fila superior
monsters = [] #lista para almacenar objetos de monstruos
for j in range(3): #ciclo por las columnas
   y = start_y + (55 * j) #coordenada del monstruo en cada columna siguiente será compensada por 55 píxeles en y
   x = start_x + (27.5 * j) # 27.5 x
   for i in range (count):#un ciclo a través de las filas (líneas) crea un número de monstruos en una fila igual a count
       d = Picture('enemy.png', x, y, 50, 50) #creando un monstruo
       monsters.append(d) #añadiendo a la lista
       x = x + 55 #aumentando la coordenada del siguiente monstruo
   count = count - 1 #para la siguiente fila, reduce el número de monstruos


while not game_over:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
   ball.fill()
   platform.fill()

   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           game_over = True
#dibujando todos los monstruos de la lista
   for m in monsters:
       m.draw()
   platform.draw()
   ball.draw()
   pygame.display.update()
   clock.tick(40)
