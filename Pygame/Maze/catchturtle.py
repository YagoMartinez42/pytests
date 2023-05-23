from turtle import Turtle

class Sprite(Turtle):
    def __init__(self, x, y, step, shape, color):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
    def check_collission(self, other_object):
        dist = self.distance(other_object.xcor(), other_object.ycor())
        if dist < 15:
            return True
        else:
            return False

class Player(Sprite):
    def __init__(self, x, y, step=10, shape = 'circle', color = 'orange'):
        super().__init__(x, y, step, shape, color)
    def move_up(self):
        self.setheading(90)
        self.forward(self.step)
    def move_down(self):
        self.setheading(270)
        self.forward(self.step)
    def move_left(self):
        self.setheading(180)
        self.forward(self.step)
    def move_right(self):
        self.setheading(0)
        self.forward(self.step)

player1 = Player(0, -100)
target1 = Sprite(0, 200, 5, 'arrow', 'green')
obstacle1 = Sprite(200, 0, 5, 'square', 'red')
obstacle2 = Sprite(-200, 0, 5, 'square', 'red')

scr = player1.getscreen()
scr.listen()
scr.onkey(player1.move_up, 'Up')
scr.onkey(player1.move_left, 'Left')
scr.onkey(player1.move_right, 'Right')
scr.onkey(player1.move_down, 'Down')

total_score = 0
while total_score < 3:
    if player1.check_collission(target1):
        player1.goto(0, -100)
        total_score += 1
    if player1.check_collission(obstacle1) or player1.check_collission(obstacle2):
        target1.hideturtle()
        break
obstacle1.hideturtle()
obstacle2.hideturtle()
