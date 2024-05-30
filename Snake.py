from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in START:
            self.add_seg(position)

    def add_seg(self, position):
        segment = Turtle()
        segment.color("white")
        segment.shape("square")
        segment.penup()
        segment.setposition(position)
        self.snake.append(segment)

    def extend(self):
        self.add_seg(self.snake[-1].position())

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(20)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)

    def left(self):
        self.head.setheading(LEFT)

    def right(self):
        self.head.setheading(RIGHT)
