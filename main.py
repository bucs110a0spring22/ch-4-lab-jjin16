import turtle
import math
import time
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
ORIGIN=(0,0)
RIGHT_ANGLE=90
#part A
def drawSineCurve(dart,degree_max= 360,degree_min= -360):
  """
  draws the sine curve 
  arg: turtle object
  return: ()none
  """
  dart.pu()
  dart.goto(ORIGIN)
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
  dart.goto(ORIGIN[0], y_max)
  dart.goto(ORIGIN[0],y_min)
  dart.goto(ORIGIN)
  dart.goto(degree_max, ORIGIN[1])
  dart.goto(degree_min,ORIGIN[1])
  dart.goto(ORIGIN)
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
  dart.goto(ORIGIN)
  dart.pencolor("purple")
  dart.pd()
  for degree in range (degree_min, degree_max):
    y= math.tan(math.radians(degree))
    dart.goto(degree, y)
  dart.pu()
def draw_pixel_of_same_color(dart, color="black", line_length=0, pixel_size=5):
  """
  draws the horizontal line of sans drawing 
  arg: (dart)turtle object, (color)string that represents the color of the horizontal line, (line_length)the length of the horizontal line, (pixel_size) size of the pixel in the pixel drawing.
  return: ()none
  """
  dart.pencolor(color)
  dart.pd()
  dart.fillcolor(color)
  dart.begin_fill()
  number_of_half_rectangle=2
  for sides in range(number_of_half_rectangle):
    dart.fd(line_length*pixel_size)
    dart.rt(RIGHT_ANGLE)
    dart.fd(pixel_size)
    dart.rt(RIGHT_ANGLE)
  dart.end_fill()
  dart.pu()
  dart.fd(line_length*pixel_size)
def go_empty_pixel_line(dart, line_length=0, pixel_size=5):
  """
  moves the turtle object without drawing, represents the no color pixels 
  arg: (dart)turtle object,(line_length)the length of the horizontal line, (pixel_size) size of the pixel in the pixel drawing.
  return: ()none
  """
  dart.pu()
  dart.fd(line_length*pixel_size)
def draw_line_of_pixels(dart, line_length=0, color="black", pixel_size=5):
  """
  draws the line of pixels with colors depending on the parameters.
  arg: (dart)turtle object,(line_length)the length of the horizontal line,(color)string that represents the color of the horizontal line (pixel_size) size of the pixel in the pixel drawing.
  return: ()none
  """
  if color=="empty":
    go_empty_pixel_line(dart, line_length)
  else:
    draw_pixel_of_same_color(dart, color, line_length, pixel_size)
def switch_lane(dart, pixel_size=5):
  """
  moves the turtle object to the next horizontal line of the drawing(downwards)
  arg: (dart)turtle object, (pixel_size) size of the pixel in the pixel drawing.
  return: ()none
  """
  dart.pu()
  dart.rt(RIGHT_ANGLE)
  dart.fd(pixel_size)
  dart_position= dart.position()
  dart_position_y= dart_position[1]
  dart.goto(ORIGIN[0], dart_position_y)
  dart.lt(RIGHT_ANGLE)
def ask_user_to_see_drawing():
  """
  asks the user if they want to see a drawing of sans.
  arg: ()none
  return: boolean True/False
  """
  user_answer=input("Hey, do you want to see a picture of sans? y/n:")
  if user_answer=="y" or user_answer=="Y":
    print("Okay!")
    return True
  else:
    print("are you sure? you're missing out!")
    return False
def draw_sans():
  """
  assembles the defined functions and adds specific parameters to draw the picture of sans.
  arg: ()none
  return: ()none
  """
  wn=turtle.Screen()
  wn.setworldcoordinates(0,-150,115,0)
  wn.bgcolor("grey")
  dart= turtle.Turtle()
  dart.speed(0)
  draw_line_of_pixels(dart,7,"empty")
  draw_line_of_pixels(dart,9,"black")
  switch_lane(dart)#line 1 finish
  draw_line_of_pixels(dart,5,"empty")
  draw_line_of_pixels(dart,2,"black")
  draw_line_of_pixels(dart,9,"white")
  draw_line_of_pixels(dart,2,"black")
  switch_lane(dart)#line 2 finish
  for i in range(2):
    draw_line_of_pixels(dart,4,"empty")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,13,"white")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 3 finish
    draw_line_of_pixels(dart,3,"empty")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,15,"white")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 5 finish
  for i in range(2):
    draw_line_of_pixels(dart,3,"empty")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,2,"white")
    draw_line_of_pixels(dart,3,"black")
    draw_line_of_pixels(dart,5,"white")
    draw_line_of_pixels(dart,3,"black")
    draw_line_of_pixels(dart,2,"white")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 6 finish
    #line 7 finish
  draw_line_of_pixels(dart,3,"empty")
  draw_line_of_pixels(dart,1,"black")
  draw_line_of_pixels(dart,2,"white")
  draw_line_of_pixels(dart,3,"black")
  draw_line_of_pixels(dart,2,"white")
  draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,2,"white")
    draw_line_of_pixels(dart,3,"black")
    draw_line_of_pixels(dart,2,"white")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 8 finish
    draw_line_of_pixels(dart,4,"empty")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,5,"white")
    draw_line_of_pixels(dart,3,"black")
    draw_line_of_pixels(dart,5,"white")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 9 finish
    draw_line_of_pixels(dart,3,"empty")
    draw_line_of_pixels(dart,2,"black")
    draw_line_of_pixels(dart,1,"white")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,9,"white")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,1,"white")
    draw_line_of_pixels(dart,2,"black")
    switch_lane(dart)#line 10 finish
    draw_line_of_pixels(dart,3,"empty")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,2,"white")
    draw_line_of_pixels(dart,11,"black")
    draw_line_of_pixels(dart,2,"white")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 11 finish
    draw_line_of_pixels(dart,3,"empty")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,3,"white")
    for i in range(5):
      draw_line_of_pixels(dart,1,"black")
      draw_line_of_pixels(dart,1,"white")
    draw_line_of_pixels(dart,2,"white")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 12 finish
    draw_line_of_pixels(dart,4,"empty")
    draw_line_of_pixels(dart,2,"black")
    draw_line_of_pixels(dart,2,"white")
    draw_line_of_pixels(dart,7,"black")
    draw_line_of_pixels(dart,2,"white")
    draw_line_of_pixels(dart,2,"black")
    switch_lane(dart)#line 13 finish
    draw_line_of_pixels(dart,3,"empty")
    draw_line_of_pixels(dart,5,"black")
    draw_line_of_pixels(dart,7,"white")
    draw_line_of_pixels(dart,5,"black")
    switch_lane(dart)#line 14 finish
    draw_line_of_pixels(dart,2,"empty")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,1,"blue")
    draw_line_of_pixels(dart,15,"black")
    draw_line_of_pixels(dart,1,"blue")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 15 finish
    draw_line_of_pixels(dart,1,"empty")
    draw_line_of_pixels(dart,2,"black")
    draw_line_of_pixels(dart,1,"blue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,2,"skyblue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,3,"white")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,3,"white")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,2,"skyblue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,1,"blue")
    draw_line_of_pixels(dart,2,"black")
    switch_lane(dart)#line 16 finish
    draw_line_of_pixels(dart,1,"empty")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,3,"blue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,2,"skyblue")
    draw_line_of_pixels(dart,3,"black")
    draw_line_of_pixels(dart,1,"white")
    draw_line_of_pixels(dart,3,"black")
    draw_line_of_pixels(dart,2,"skyblue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,3,"blue")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 17 finish
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,2,"blue")
    draw_line_of_pixels(dart,2,"black")
    draw_line_of_pixels(dart,1,"blue")
    draw_line_of_pixels(dart,3,"black")
    draw_line_of_pixels(dart,2,"white")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,2,"white")
    draw_line_of_pixels(dart,3,"black")
    draw_line_of_pixels(dart,1,"blue")
    draw_line_of_pixels(dart,2,"black")
    draw_line_of_pixels(dart,2,"blue")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 18 finish
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,4,"blue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,2,"blue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,5,"white")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,2,"blue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,4,"blue")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 19 finish
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,5,"blue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,1,"blue")
    draw_line_of_pixels(dart,2,"black")
    draw_line_of_pixels(dart,3,"white")
    draw_line_of_pixels(dart,2,"black")
    draw_line_of_pixels(dart,1,"blue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,5,"blue")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 20 finish
    draw_line_of_pixels(dart,1,"empty")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,3,"blue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,2,"blue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,5,"white")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,2,"blue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,3,"blue")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 21 finish
    draw_line_of_pixels(dart,2,"empty")
    draw_line_of_pixels(dart,2,"black")
    draw_line_of_pixels(dart,1,"blue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,2,"blue")
    draw_line_of_pixels(dart,7,"black")
    draw_line_of_pixels(dart,2,"blue")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,1,"blue")
    draw_line_of_pixels(dart,2,"black")
    switch_lane(dart)#line 22 finish
    draw_line_of_pixels(dart,3,"empty")
    draw_line_of_pixels(dart,3,"black")
    draw_line_of_pixels(dart,2,"blue")
    draw_line_of_pixels(dart,7,"black")
    draw_line_of_pixels(dart,2,"blue")
    draw_line_of_pixels(dart,3,"black")
    switch_lane(dart)#line 23 finish
    draw_line_of_pixels(dart,3,"empty")
    draw_line_of_pixels(dart,17,"black")
    switch_lane(dart)#line 24 finish
    draw_line_of_pixels(dart,2,"empty")
    draw_line_of_pixels(dart,19,"black")
    switch_lane(dart)#line 25 finish
    draw_line_of_pixels(dart,2,"empty")
    draw_line_of_pixels(dart,9,"black")
    draw_line_of_pixels(dart,1,"empty")
    draw_line_of_pixels(dart,9,"black")
    switch_lane(dart)#line 26 finish
    draw_line_of_pixels(dart,3,"empty")
    draw_line_of_pixels(dart,7,"black")
    draw_line_of_pixels(dart,3,"empty")
    draw_line_of_pixels(dart,7,"black")
    switch_lane(dart)#line 27 finish
    draw_line_of_pixels(dart,1,"empty")
    draw_line_of_pixels(dart,3,"black")
    draw_line_of_pixels(dart,5,"white")
    draw_line_of_pixels(dart,3,"empty")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,5,"white")
    draw_line_of_pixels(dart,3,"black")
    switch_lane(dart)#line 28 finish
    draw_line_of_pixels(dart,1,"empty")
    draw_line_of_pixels(dart,1,"black")
    draw_line_of_pixels(dart,6,"white")
    draw_line_of_pixels(dart,2,"black")
    draw_line_of_pixels(dart,3,"empty")
    draw_line_of_pixels(dart,2,"black")
    draw_line_of_pixels(dart,7,"white")
    draw_line_of_pixels(dart,1,"black")
    switch_lane(dart)#line 29 finish
    draw_line_of_pixels(dart,2,"empty")
    draw_line_of_pixels(dart,6,"black")
    draw_line_of_pixels(dart,7,"empty")
    draw_line_of_pixels(dart,7,"black")
    #line 30 finish
    #wn.exitonclick()
def ask_to_draw_sans():
  """
  calls the function that asks the user if they want to see a drawing of sans. then responds depending on the user's answer
  arg: ()none
  return: ()none
  """
  time_waiting=3
  user_decision= ask_user_to_see_drawing()
  if user_decision== True:
    draw_sans()
  else:
    time.sleep(time_waiting)
    print("I'm sorry. You have no choice but to look at this sans drawing of sans. ;)")
    draw_sans()
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
  dart.clear()
  ask_to_draw_sans()
  #draw_sans()
  wn.exitonclick()
main()
