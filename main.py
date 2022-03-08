import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
#part A
def drawSineCurve(dart):
  """
  draws the sine curve 
  arg: turtle object
  return: ()none
  """
  degree_max= 360
  degree_min= -360
  dart.pu()
  dart.goto(0,0)
  dart.pencolor("blue")
  dart.pd()
  for degree in range (degree_min, degree_max):
    y = math.sin(math.radians(degree))
    dart.goto(degree, y)
  dart.pu()
#part B
def setupWindow(wn):
  """
  sets up the canvas(window) size so the graph is easier to view
  arg: window object
  return: ()none
  """
  degree_max= 360
  degree_min= -360
  y_max= 10
  y_min= -10
  wn.setworldcoordinates(degree_min,y_min, degree_max, y_max)
def setupAxis(dart):
  """
  draws the x-y axis for the graph
  arg: turtle object 
  return: ()none
  """
  degree_max= 360
  degree_min= -360
  y_max= 10
  y_min= -10
  dart.pencolor("black")
  dart.pd()
  dart.goto(0, y_max)
  dart.goto(0,y_min)
  dart.goto(0,0)
  dart.goto(degree_max, 0)
  dart.goto(degree_min,0)
  dart.goto(0,0)
  dart.pu()
def drawCosineCurve(dart):
  """
  draws the cosine curve 
  arg: turtle object
  return: ()none
  """
  degree_max= 360
  degree_min= -360
  dart.pu()
  dart.pencolor("red")
  for degree in range (degree_min, degree_max):
    y = math.cos(math.radians(degree))  
    if degree == degree_min:
        dart.goto(degree, y)
        dart.pd()
    dart.goto(degree, y)
  dart.pu()
def drawTangentCurve(dart):
  """
  draws the tangent curve 
  arg: turtle object
  return: ()none
  """
  degree_max= 360
  degree_min= -360
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
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
