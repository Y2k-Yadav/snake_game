from turtle import Screen, Turtle
from food import Food
from snake import Snake
import time

turtle = Turtle()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
# move snake
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food)<15:
        food.refresh()
screen.exitonclick()
