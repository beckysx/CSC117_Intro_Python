# Xu Song
# Lab 11: graphics


import time  # we need a brief delay
from graphics import *  # imports graphics libraty

# Step 1

# set some params
windowWidth = 400
windowHeight = 400
windowTitle = 'Super window!!'

# create the graphics window object
print('Creating Graphics object')
win = GraphWin(windowTitle, windowWidth, windowHeight)

# Step 2

# centerpoint
win.setCoords(0, 0, 100, 100)
print('Draw a point')
centerPoint = Point(50, 50)
centerPoint.draw(win)
# draw circle
myCircle = Circle(centerPoint, 10)
myCircle.draw(win)
# color
myCircle.setFill('purple')

anotherPoint = Point(10, 10)
anotherCircle = Circle(anotherPoint, 10)
anotherCircle.setFill('black')
anotherCircle.draw(win)

# make the black circle float across the screen
##for i in range(100):
##    anotherCircle.move(1,1)
##    clicked=win.getMouse()
##    x=clicked.getX()#get x coord
##    y=clicked.getY()#get y coord
##    print(x,y)
##    time.sleep(0.1)

# Step 3
# draw griglines

color = 'red'
clicked = win.checkMouse()
while not clicked:
    anotherCircle.move(0.5, 0.5)
    if color == 'red':
        color = 'blue'
    else:
        color = 'red'
    anotherCircle.setFill(color)
    time.sleep(0.025)
    clicked = win.checkMouse()

# wait until the user clics mouse then close win
print('Click window anywhere to end')
win.getMouse()  # stop the presses!
win.close()  # this closes the window
print('Program is over !Goodbye')
