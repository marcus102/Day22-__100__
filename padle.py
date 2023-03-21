from turtle import Turtle

class Padle(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('square')
    self.penup()
    self.color('white')
    self.turtlesize(stretch_wid=5, stretch_len=1)
    
    
  def position(self,x_position, y_position):
    self.goto(x_position, y_position)
    
    
  def down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)
    
    
  def up(self):
      new_y = self.ycor() + 20
      self.goto(self.xcor(), new_y)