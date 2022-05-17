from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


SCREEN_SIZE = 600
VELOCITY = 13
screen = Screen()
screen.setup(height=SCREEN_SIZE, width=SCREEN_SIZE)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

pause_screen = Turtle()
pause_screen.hideturtle()


def pause():
    global paused
    if not paused:
        pause_screen.color("white")
        pause_screen.write("Pause", align="center", font=("Courier", 18, "normal"))
        paused = True
    else:
        pause_screen.clear()
        paused = False


screen.onkey(pause, "space")

paused = False
game_is_on = True
while game_is_on:
    if not paused:
        screen.update()
        time.sleep(1/VELOCITY)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.add_score()

        # Detect collision with the wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

        # Detect collision with the tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset_scoreboard()
                snake.reset_snake()
    else:
        screen.update()

screen.exitonclick()
