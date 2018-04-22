import turtle
from threading import Timer
import random
import time
random.seed(time.time())
# Create the window
win = turtle.Screen()
win.bgcolor("black")
win.title("Stupid Fucking Maze")
win.setup(700, 700)

# Create the Pen class which is a child of Turtle class
class Pen(turtle.Turtle):
    #constructor
    def __init__(self):
        # initialize the parent class
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        # to avoid leaving trail behind
        self.penup()
        # the speed of the animation
        self.speed(0)

# Create the Player class which is a child of Turtle class
class Player(turtle.Turtle):
    def __init__(self, color):
        # initialize the parent class
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color(color)
        self.penup()
        self.speed(0)

    # Player has 4 directions to go: up, down, left, right
    def goUp(self):
        global winner
        if ((self.xcor(), self.ycor() + 24) not in walls):
            self.goto(self.xcor(), self.ycor() + 24)

        if ((self.xcor(), self.ycor() + 24) ==  winner):
            print("YOU WIN, Im a lazy shit who didn't want to put this on the actual screen")
        
    def goDown(self):
        global winner
        if ((self.xcor(), self.ycor() - 24) not in walls):
            self.goto(self.xcor(), self.ycor() - 24)
        if ((self.xcor(), self.ycor() - 24) ==  winner):
            print("YOU WIN, Im a lazy shit who didn't want to put this on the actual screen")

    def goLeft(self):
        global winner
        if ((self.xcor()-24, self.ycor()) not in walls):
            self.goto(self.xcor()-24, self.ycor())

        if ((self.xcor() -24, self.ycor()) ==  winner):
            print("YOU WIN, Im a lazy shit who didn't want to put this on the actual screen")
    def goRight(self):
        global winner
        if ((self.xcor()+24, self.ycor()) not in walls):
            self.goto(self.xcor()+24, self.ycor())

        if ((self.xcor()+24, self.ycor()) ==  winner):
            print("YOU WIN, Im a lazy shit who didn't want to put this on the actual screen")


# Create levels
# start level list empty to start level 1 at 1
levels = [""]

#Level 1
level1 = [
"XXXXXXXXXXXXXXXXXXXXXXXX", 
"XP                XXXXXX", 
"XXXXX XXXX XXXXXX XXXXXX",
"XXXXX XXXX XXXXXX XXXXXX",
"XXXXXXXX   XXXX     XXXX",
"XXXXXXXXX XXX XXX    XXX",
"XXXXXXXXX XXX XXX XX XXX",
"XXXXXXXXX XXX     XX XXX", 
"XX        XXXXXXX XX XXX", 
"XX XXXXXX XXXXXXX XX XXX",
"XX XX XXX XXXXXXXXXX XXX", 
"XX XX XXX XXXXXXXXXX XXX", 
"XX XX XXX     XXXXXX XXX",
"XX XX XXX XXX X      XXX",
"XX       XXXX X   XXX XX",
"XX XXXXXXXXXX XXXXXXX XX",
"XX XXXXXX         XXX XX",
"XX X   XX XXXXXXX     XX", 
"XX   X XX XXXXXXX XXXXXX", 
"XXXXXX XX     XXX XXXXXX",
"X   XX XX  XX XXX XXXXXX",
"XXX XX XXXXXX XXX XXXXXX",
"XXX XX XXXX   XXX   XXXX",
"XXX     XXXX XXXXXXWXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX"
]


# Append each level to the levels list
levels.append(level1)
winner = (0, 0)

# Function to set up the maze
# Loops through all rows and columns to set up maze
def setupMaze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # get the character at each cell of the grid
            character = level[y][x]
            # translate axis 0,0 at top left corner to our axis 0,0 in center
            # in our axis: 0,0 in center and -288, 288 top left corner
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # If the character is an X, we want to move the pen there and stamp
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y)) 

            # If the character is a P, the player should go here.
            if character == "P":
                player.goto(screen_x, screen_y)
            if character == "W":
                global winner
                winner = (screen_x, screen_y)
                end.goto((screen_x, screen_y))

# Create objects
pen = Pen()
player = Player("Red")
end = Player("White")

# Create list with all the wall coordinates with the screen coordinates
walls = []

# Set up the level
setupMaze(levels[1])

# Keyboard Binding
turtle.listen()
turtle.onkey(player.goLeft, "Left")
turtle.onkey(player.goRight, "Right")
turtle.onkey(player.goDown, "Down")
turtle.onkey(player.goUp, "Up")

# Turn off screen updates?
win.tracer(0)



# List of modes
norm = ("Left", "Right", "Up", "Down")
vim = ("h","l","j","k" )
letters = ("l","r","u","d")
inverse = ("Right", "Left", "Down", "Up")
asdw = ("a", "d", "w", "s")
dwsa = ("d", "a", "s", "w")
nums = ("1", "2", "3", "4")
pi = ("3", "1", "4", "5")

modes = []
modes.append(norm)
modes.append(vim)
modes.append(letters)
modes.append(inverse)
modes.append(asdw)
modes.append(dwsa)
modes.append(nums)
modes.append(pi)

tags = []
tags.append("Norm")
tags.append("Vim")
tags.append("First Letter")
tags.append("Inverse")
tags.append("Gamer")
tags.append("Drunk Gamer")
tags.append("Numbers")
tags.append("Pie")


resetKeys = 0

def nothing():
    pass

def changeMode():
    turtle.clear()
    global resetKeys
    rand = random.randint(0,7)
    selectMode = modes[resetKeys]
    turtle.onkey(nothing, selectMode[0])
    turtle.onkey(nothing, selectMode[1])
    turtle.onkey(nothing, selectMode[2])
    turtle.onkey(nothing, selectMode[3])
    selectMode = modes[rand]
    resetKeys = rand
    turtle.onkey(player.goLeft, selectMode[0])
    turtle.onkey(player.goRight, selectMode[1])
    turtle.onkey(player.goUp, selectMode[2])
    turtle.onkey(player.goDown, selectMode[3])
    modeStr = tags[rand]
    print("Mode changed to %s" % modeStr)
    turtle.write("Mode changed to %s" % modeStr, True, align="center",font=("Arial", 15, "normal"))

turtle.penup()
turtle.setx(-288)
turtle.sety(298)
turtle.pendown()
turtle.pencolor("red")
count = 0 
timer = 1000
# Main game loop
while True:
    count += 1
    if (count > timer):
        changeMode()
        count = 0
        timer -= 50
    win.update()
