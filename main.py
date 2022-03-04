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
  dart.pu()
  dart.goto(0,0)
  dart.pencolor("blue")
  dart.pd()
  #accumulator_for_x= 0
  for degree in range (-360, 360+1):
    y = math.sin(math.radians(degree))
    #x= accumulator_for_x
    #print(x)#debug
    #print(y)#debug
    dart.goto(degree, y)
    #accumulator_for_x+= 1
  dart.pu()
#part B
def setupWindow(wn):
  """
  sets up the canvas(window) size so the graph is easier to view
  arg: window object
  return: ()none
  """
  wn.setworldcoordinates(-360-10, -10, 360+10, 11)
def setupAxis(dart):
  """
  draws the x-y axis for the graph
  arg: turtle object 
  return: ()none
  """
  dart.pencolor("black")
  dart.pd()
  dart.goto(0, 10)
  dart.goto(0,-10)
  dart.goto(0,0)
  dart.goto(360+10, 0)
  dart.goto(-360-10,0)
  dart.goto(0,0)
  dart.pu()
def drawCosineCurve(dart):
  """
  draws the cosine curve 
  arg: 
  return: ()none
  """
  dart.pu()
  #dart.goto(-360,1)
  dart.pencolor("red")
  #dart.pd()
  #accumulator_for_x= 0
  for degree in range (-360, 360+1):
    y = math.cos(math.radians(degree))  
    if degree == -360:
        dart.goto(degree, y)
        dart.pd()
    #dart.pd()
    #y = math.cos(math.radians(degree))
    #x= accumulator_for_x
    #print(x)#debug
    #print(y)#debug
    dart.goto(degree, y)
    #accumulator_for_x+= 1
  dart.pu()
def drawTangentCurve(dart):
  """
  draws the tangent curve 
  arg: 
  return: ()none
  """
  dart.pu()
  dart.goto(0,0)
  dart.pencolor("purple")
  dart.pd()
  #accumulator_for_x= 0
  for degree in range (-360, 360+1):
    y= math.tan(math.radians(degree))
    #x= accumulator_for_x
    #print(x)#debug
    #print(y)#debug
    dart.goto(degree, y)
    #accumulator_for_x+= 1
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
