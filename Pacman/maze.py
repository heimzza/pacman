import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Pacman Game")
wn.setup(700, 700)

images = ["pac_left.gif", "pac_right.gif", "pac_down.gif", "pac_up.gif",
          "fruit_cherry.gif", "fruit_orange.gif", "fruit_strawberry.gif",
          "ghost_blue.gif"]
for image in images:
    turtle.register_shape(image)


# Create class Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


# Create class Player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("pac_down.gif")
        self.color("dark blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        self.shape("pac_up.gif")

        if(move_to_x, move_to_y) not in walls:
            self.goto(self.xcor(), self.ycor() + 24)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        self.shape("pac_down.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(self.xcor(), self.ycor() - 24)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        self.shape("pac_right.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(self.xcor() + 24, self.ycor())

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        self.shape("pac_left.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(self.xcor() - 24, self.ycor())

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


# Create class Enemy
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("ghost_blue.gif")
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        # Calculate the position change
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])

        wn.ontimer(self.move, t=random.randint(100, 300))

# Create class Orange
class Orange(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("fruit_orange.gif")
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.gold = 3

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Create class Strawberry
class Strawberry(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("fruit_strawberry.gif")
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.gold = 5

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Create class Cherry
class Cherry(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("fruit_cherry.gif")
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.gold = 7

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


levels = [""]
walls = []
foods = []
enemies = []

level_1 = [
            "XXXXXXXXXXXXXXXXXXXXXXXX",
            "X  E  XX   XX       X  X",
            "X  X  XXX  XX  XXX  X  X",
            "X  X       XX   XX  X  X",
            "X  X  XXX  XX   XX  X  X",
            "X          XX  XXX  X  X",
            "X  X  XXX  XX  XXX  E  X",
            "X  X  XXX  XX   XX  X  X",
            "X  X E   XXXX   XX  X  X",
            "XXXX                X  X",
            "X  XXXXXXXXXX S XXXXXXXX",
            "X  XX      XX   XXX    X",
            "X           X   XXX    X",
            "X  XXXXXXX  X C XXXX  XX",
            "X  XXXXXXX  X   XXXX  XX",
            "X  XXXXXXX      XXXX  XX",
            "X  XXXXXXX  X   XXXX  XX",
            "X     P     X   XXXX  XX",
            "X  XXXXXXX  X S XXXX EXX",
            "X  XXXXXXX  X   XXXX  XX",
            "X  XXXXX    X   XXXX  XX",
            "X               XXXX  XX",
            "X  XXXXXX   X         XX",
            "XXXXXXXXXXXXXXXXXXXXXXXX"
         ]

level_2 = [
            "XXXXXXXXXXXXXXXXXXXXXXXX",
            "X     XX   XX  E    X  X",
            "X  X  XXX  XX  XXX  X  X",
            "X  X     E XX   XX  X  X",
            "X  X  XXX  XX   XX  X  X",
            "X          XX  XXX  X  X",
            "X  X  XXX  XX  XXX     X",
            "X  X  XXX  XX   XX  X  X",
            "X  X     XXXX   XX  X  X",
            "XXXX           P    X  X",
            "X  XXXXXXXXXX   XXXXXXXX",
            "X  XX      XX   XXX    X",
            "X   E       X   XXX    X",
            "X  XXXXXXX  X   XXXX  XX",
            "X  XXXXXXX  X   XXXX  XX",
            "X  XXXXXXX      XXXX  XX",
            "X  XXXXXXX  X   XXXX  XX",
            "X           X   XXXX  XX",
            "X  XXXXXXX  X   XXXX  XX",
            "X  XXXXXXX  X   XXXX  XX",
            "X  XXXXX    X   XXXX  XX",
            "X      E        XXXX  XX",
            "XC XXXXXX   X     S    X",
            "XXXXXXXXXXXXXXXXXXXXXXXX"
         ]

level_3 = [
            "XXXXXXXXXXXXXXXXXXXXXXXX",
            "XX     E      CS      XX",
            "XXXXXXXXXX  XXX  XXX  XX",
            "XXXXXX  XX  XXX  XXX  XX",
            "XX E    O        XXX  XX",
            "XXXXXX  XX  XXXXXXXX  XX",
            "XX  XX  XX  XXXXXXXX  XX",
            "XX  XX  XX            XX",
            "XX P     XXXXX  XXXX  XX",
            "XX  XXXXXXXXXX  XXXX  XX",
            "XX  XXXX  XXXX  XXXX  XX",
            "XX  XXXX  XXXX  XXXX  XX",
            "XX                 X  XX",
            "XX  XXXXXXXXXXXXX  X  XX",
            "XX  X  XXXXX       X  XX",
            "XX  X  XXXXX  XXXXXX  XX",
            "XX   E           XXX  XX",
            "XX  XXXXXXXXXXX  XXX  XX",
            "XX  XXXX    XX        XX",
            "XX  XXXX  XXXXX  XXXXXXX",
            "XX         E          XX",
            "XX  XXXX  XXXXX  XXX  XX",
            "XX  XXXX  XXXXX  XXX  XX",
            "XXXXXXXXXXXXXXXXXXXXXXXX"
           ]

level_4 = [
            "XXXXXXXXXXXXXXXXXXXXXXXX",
            "XX     E   C          XX",
            "XXXXXXXXXX  XXX  XXX  XX",
            "XXXXXX  XX  XXX  XXX  XX",
            "XX               XXX  XX",
            "XXXXXX  XX  XXXXXXXX  XX",
            "XX  XX  XX  XXXXXXXX  XX",
            "XX  XX  XX            XX",
            "XX       XXXXX  XXXX  XX",
            "XX  XXXXXXXXXX  XXXX  XX",
            "XX  XXXX  XXXX  XXXX  XX",
            "XX  XXXX  XXXX  XXXX  XX",
            "XX              E  X  XX",
            "XX  XXXXXXXXXXXXX  X  XX",
            "XX  X  XXXXX       X  XX",
            "XX  X  XXXXX  XXXXXX  XX",
            "XX      P        XXX  XX",
            "XX  XXXXXXXXXXX  XXX  XX",
            "XX  XXXX    XX        XX",
            "XX  XXXXE XXXXX  XXXXXXX",
            "XX                    XX",
            "XX  XXXX  XXXXX EXXX  XX",
            "XX  XXXX  XXXXX  XXX  XX",
            "XXXXXXXXXXXXXXXXXXXXXXXX"
           ]


levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if it is an X (Wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                # Add X'es(walls) to Walls list
                walls.append((screen_x, screen_y))

            # Check if it is a P (Player)
            if character == "P":
                player.goto(screen_x, screen_y)

            # Check if it an O (Orange)
            if character == "O":
                foods.append(Orange(screen_x, screen_y))

            # Check if it an S (Strawberry)
            if character == "S":
                foods.append(Strawberry(screen_x, screen_y))

            # Check if it an C (Cherry)
            if character == "C":
                foods.append(Cherry(screen_x, screen_y))

            # Check if it an E (Enemy)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))


pen = Pen()
player = Player()

setup_maze(levels[3])

# Keyboard Bindings
wn.onkey(player.go_left, "a")
wn.onkey(player.go_right, "d")
wn.onkey(player.go_up, "w")
wn.onkey(player.go_down, "s")
wn.listen()

# Turn off screen updates
wn.tracer(0)

for enemy in enemies:
    wn.ontimer(enemy.move(), t=250)
# Main game loop
while True:
    # Checking for player collision with food
    for food in foods:
       if player.is_collision(food):
            # Add golds to players gold
            player.gold += food.gold
            print("Player gold : {}".format(player.gold))
            # Destroy the food
            food.destroy()
            # Removing from food list
            foods.remove(food)
    for enemy in enemies:
        if player.is_collision(enemy):
            print("Game Over")


    # Update Screen
    wn.update()
