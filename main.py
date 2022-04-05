import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
#part A
def drawSineCurve(dart,degree_max= 360,degree_min= -360):
  """
  draws the sine curve 
  arg: turtle object
  return: ()none
  """
  dart.pu()
  dart.goto(0,0)
  dart.pencolor("blue")
  dart.pd()
  for degree in range (degree_min, degree_max):
    y = math.sin(math.radians(degree))
    dart.goto(degree, y)
  dart.pu()
#part B
def setupWindow(wn,degree_max= 360,degree_min= -360,y_max= 10,y_min= -10):
  """
  sets up the canvas(window) size so the graph is easier to view
  arg: window object
  return: ()none
  """
  wn.setworldcoordinates(degree_min,y_min, degree_max, y_max)
def setupAxis(dart,degree_max= 360,degree_min= -360,y_max= 10,y_min= -10):
  """
  draws the x-y axis for the graph
  arg: turtle object 
  return: ()none
  """
  dart.pencolor("black")
  dart.pd()
  dart.goto(0, y_max)
  dart.goto(0,y_min)
  dart.goto(0,0)
  dart.goto(degree_max, 0)
  dart.goto(degree_min,0)
  dart.goto(0,0)
  dart.pu()
def drawCosineCurve(dart,degree_max= 360,degree_min= -360):
  """
  draws the cosine curve 
  arg: turtle object
  return: ()none
  """
  dart.pu()
  dart.pencolor("red")
  for degree in range (degree_min, degree_max):
    y = math.cos(math.radians(degree))  
    if degree == degree_min:
        dart.goto(degree, y)
        dart.pd()
    dart.goto(degree, y)
  dart.pu()
def drawTangentCurve(dart,degree_max= 360,degree_min= -360):
  """
  draws the tangent curve 
  arg: turtle object
  return: ()none
  """
  dart.pu()
  dart.goto(0,0)
  dart.pencolor("purple")
  dart.pd()
  for degree in range (degree_min, degree_max):
    y= math.tan(math.radians(degree))
    dart.goto(degree, y)
  dart.pu()
##########  Do Not Alter Any Code Past Here ########
def main():
  degree_max= 360
  degree_min= -360
  y_max= 10
  y_min= -10
  #Part A
  wn = turtle.Screen()
  wn.tracer(5)
  dart = turtle.Turtle()
  dart.speed(0)
  drawSineCurve(dart,degree_max,degree_min)
  #Part B
  setupWindow(wn,degree_max,degree_min,y_max,y_min)
  setupAxis(dart,degree_max,degree_min,y_max,y_min)
  dart.speed(0)
  drawSineCurve(dart,degree_max,degree_min)
  drawCosineCurve(dart,degree_max,degree_min)
  drawTangentCurve(dart,degree_max,degree_min)
  wn.exitonclick()
main()
