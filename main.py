from turtle import Screen
from padle import Padle
import time
from ball import Ball
from score_board import Scores

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Arcade Game')
screen.tracer(0)
score_board = Scores()


r_padle = Padle()
r_padle.position(350, 0)

l_padle = Padle()
l_padle.position(-350, 0)

ball = Ball()

screen.listen()
screen.onkey(r_padle.down, 'Down')
screen.onkey(r_padle.up, 'Up')

screen.onkey(l_padle.down, 's')
screen.onkey(l_padle.up, 'w')

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(ball.move_speed)
  ball.move()
  
  if ball.ycor() >= 290 or ball.ycor() <= -290:
    ball.bounce_y()
  
  if ball.distance(r_padle) < 50 and ball.xcor() > 320 or ball.distance(l_padle) < 50 and ball.xcor() < -320:
    ball.bounce_x()
    
  if ball.xcor() > 380:
    ball.reset_position()
    score_board.l_point()
    
  if ball.xcor() < -380:
    ball.reset_position()
    score_board.r_point()
    
    
screen.exitonclick()