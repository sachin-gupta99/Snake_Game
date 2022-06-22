import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


turtle.tracer(0)
s = turtle.Screen()
s.setup(width=588, height=600)
s.title("Snake Game")
s.bgcolor("light green")

t = turtle.Turtle()
t.hideturtle()
t.pu()
t.goto((-290, 270))
for _ in range(30):
    t.pd()
    t.forward(10)
    t.pu()
    t.forward(10)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
game = True

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.right, "Right")
s.onkey(snake.left, "Left")


while game:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1
        scoreboard.write_score()

    if abs(snake.head.xcor()) > 290 or snake.head.ycor() > 270 or snake.head.ycor() < -290:
        game = False
        scoreboard.game_over()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game = False
            scoreboard.game_over()


s.exitonclick()
