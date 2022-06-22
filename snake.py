import turtle
MOVING_DISTANCE = 23
OFFSET = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("red")

    def create_snake(self):
        offset = OFFSET
        for _ in range(3):
            self.add((-offset, 0))
            offset += 20

    def add(self, position):
        t1 = turtle.Turtle("square")
        t1.color("white")
        t1.pu()
        t1.setposition(position)
        self.segments.append(t1)

    def extend(self):
        self.add(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() == 270 or self.head.heading() == 90:
            return

        self.head.setheading(90)

    def down(self):
        if self.head.heading() == 270 or self.head.heading() == 90:
            return

        self.head.setheading(270)

    def right(self):
        if self.head.heading() == 180 or self.head.heading() == 0:
            return

        self.head.setheading(0)

    def left(self):
        if self.head.heading() == 180 or self.head.heading() == 0:
            return

        self.head.setheading(180)
