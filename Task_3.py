import turtle
# draw squares with length x and  color
def square(x,colors,times):
  t = turtle.Turtle()
  t.pendown()# to draw lines on the screen
  for j,color in enumerate(colors):
    t.pencolor(colors[j])# colours iterate through our set colours
    x = x + 10 # increase size
    for i in range(times):# iterate as many times as user has specified
      t.forward(x)# forward
      t.right(90)# 90 degree turn right 
  turtle.done()# stop drawing with pen
#draw rectangles and color where x is the length and y = x+y is breadth
def rectangle(x,colors,times,y):
  t = turtle.Turtle();
  t.pendown()
  for j,color in enumerate(colors):
    t.pencolor(colors[j])
    y = y+10
    x = x+10
    for i in range(times):
      t.forward(x)
      t.right(90)
      t.forward(y)
      t.right(90)
  turtle.done()
#draw circle with radius x
def circle(x,colors):
  t = turtle.Turtle()
  for j,color in enumerate(colors):#counter basically a loop
    t.pencolor(colors[j])
    x = x+10
    t.pendown()
    t.circle(x)
  turtle.done()

 

while True:
  choices = ['circle','square','rectangle']
  choice = input('Please enter an option between square or circle or rectangle: ')
  if choice.lower() in choices:
    break
  else:
    print("Your choice wasn't in the list of circle,square and rectangle please try again!")
    continue

colors = ['red','orange','blue','green','yellow','violet']
if choice == 'square':
  x = int(input("Please enter the length of the shape: "))
  times = int(input('how many times:'))
  square(x,colors,times)

if choice =='rectangle':
  x = int(input("Please enter the length of the shape: "))
  y = int(input("Please breadth: "))
  times =int(input('how many times:'))
  square(x,colors,times,y)

if choice =='circle': 
  x = int(input("Please enter the radius shape: "))
  times =int(input('how many times:'))
  circle(x,colors,times)