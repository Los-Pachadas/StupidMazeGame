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
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        # to avoid leaving trail behind
        self.penup()
        # the speed of the animation
        self.speed(0)


# Create levels
# start level list empty to start level 1 at 1
levels = [""]

#Level 1
level1 = [
"XXXXXXXXXXXXXXXXXXXXXXXX", 
"XP XXX            XXXXXX", 
"XX XXXXXXX XXXXXX XXXXXX",
"XX XXXXXXX XXXXXX XXXXXX",
"XX XXXXX   XXXX     XXXX",
"XX XXXXXXXXXXXXXX XXXXXX",
"XX XXXXXXXXXXXXXX XXXXXX",
"XX X          XXX XXXXXX", 
"XX XXXXXXXXXX XXX X    X", 
"XX        XXX     X XX X",
"XXX XXXXX XXXXXXX X XX X", 
"XXX XXXXX      XX X XX X", 
"XXX XXXXX XXXXXXX   XX X",
"XXX XXXXX XXXXXXXXXXXX X",
"XXX       XXXXXXXXXXXX X",
"XXXXXXXXXXXXX          X",
"XXXXXXXXXXXXX XXXXXXXXXX",
"XXXXXXXXXXXXX XXXXXXXXXX", 
"XXXX          XXXXXXXXXX", 
"XXXX XXXXXXXXXXXXXXXXXXX",
"XXXX XXXXXXXXXXXXXXXXXXX",
"XXXX XXXXXXXXXXXXXXXXXXX",
"XXXX XXXXXXXXXXXXXXXXXXX",
"XXXX XXXXXXXXXXXXXXXXXXX",
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

# Create objects
pen = Pen()

# Set up the level
setupMaze(levels[1])

# Main game loop
while True:
    pass
