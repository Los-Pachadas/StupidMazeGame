import turtle

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
    def __init__(self):
        # initialize the parent class
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)

    # Player has 4 directions to go: up, down, left, right
    def goUp(self):
        if ((self.xcor(), self.ycor() + 24) not in walls):
            self.goto(self.xcor(), self.ycor() + 24)

    def goDown(self):
        if ((self.xcor(), self.ycor() - 24) not in walls):
            self.goto(self.xcor(), self.ycor() - 24)

    def goLeft(self):
        if ((self.xcor()-24, self.ycor()) not in walls):
            self.goto(self.xcor()-24, self.ycor())

    def goRight(self):
        if ((self.xcor()+24, self.ycor()) not in walls):
            self.goto(self.xcor()+24, self.ycor())



# Create levels
# start level list empty to start level 1 at 1
levels = [""]

#Level 1
level1 = [
"XXXXXXXXXXXXXXXXXXXXXXXX", 
"XP XXX            XXXXXX", 
"XXXXXXXXXX XXXXXX XXXXXX",
"XXXXXXXXXX XXXXXX XXXXXX",
"XXXXXXXX   XXXX     XXXX",
"XXXXXXXXXXXXXXXXX XXXXXX",
"XXXXXXXXXXXXXXXXX XXXXXX",
"XXXXXXXXXXXXXXXXX XXXXXX", 
"XXXXXXXXXXXXXXXXX XXXXXX", 
"XXXXXXXXXXXXXXXXX XXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX", 
"XXXXXXXXXXXXXXXXXXXXXXXX", 
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX", 
"XXXXXXXXXXXXXXXXXXXXXXXX", 
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX"
]


# Append each level to the levels list
levels.append(level1)

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

# Create objects
pen = Pen()
player = Player()

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

# Main game loop
while True:
    win.update()
