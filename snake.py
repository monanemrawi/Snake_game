from turtle import Turtle

UP = 90 
DOWN = 270 
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.move_distance = 20
        self.head = self.squares[0]
    
    def create_snake(self):
        initial_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in initial_positions:
            self.add_square(position)
    
    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.head.forward(self.move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_square(self, position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def extend(self):
        self.add_square(self.squares[-1].position())
    
    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]
