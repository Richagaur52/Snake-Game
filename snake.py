from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_forward=20
left=0
right=180
up=90
down=270

class Snake:
    def __init__(self):
        self.new_segment = []
        self.create_snake()
        self.head=self.new_segment[0]


    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def reset_snake(self):
        for seg in self.new_segment:
            seg.goto(1000,1000)
        self.new_segment.clear()
        self.create_snake()
        self.head=self.new_segment[0]

    def add_segment(self,position):
        segment = Turtle("square")
        segment.color("white")
        segment.shapesize(stretch_wid=0.5)
        segment.penup()
        segment.goto(position)
        self.new_segment.append(segment)

    def extend(self):
        self.add_segment(self.new_segment[-1].position())

    def move(self):
        for seg_num in range(len(self.new_segment) - 1, 0, -1):
            new_x = self.new_segment[seg_num - 1].xcor()
            new_y = self.new_segment[seg_num - 1].ycor()
            self.new_segment[seg_num].goto(new_x, new_y)
        self.head.forward(move_forward)


    def move_left(self):
        if self.head.heading()!=right:
            self.head.setheading(0)

    def move_right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def move_up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def move_down(self):
        if self.head.heading() != up:
            self.head.setheading(down)





