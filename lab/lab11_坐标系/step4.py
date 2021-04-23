# Xu Song
# Lab 11: graphics


import time  # we need a brief delay
from graphics import *  # imports graphics libraty

# Step 1

# set some params
windowWidth = 400
windowHeight = 400
windowTitle = 'My graphs'

# create the graphics window object
print('Creating Graphics object')
win = GraphWin(windowTitle, windowWidth, windowHeight)

# Step 2

# centerpoint
win.setCoords(0, 0, 100, 100)
print('Draw a point')
p1 = Point(20, 50)
# draw circle
c1 = Circle(p1, 10)
c1.draw(win)

p2 = Point(20, 10)
c2 = Circle(p2, 10)
c2.draw(win)

p3 = Point(20, 30)
c3 = Circle(p3, 10)
c3.setFill('blue')
c3.draw(win)

l1 = Line(Point(10, 60), Point(10, 0))
l1.draw(win)
l2 = Line(Point(30, 60), Point(30, 0))
l2.draw(win)
l3 = Line(Point(10, 60), Point(30, 60))
l3.draw(win)
l4 = Line(Point(10, 0), Point(30, 0))
l4.draw(win)

color = 'white'
clicked = win.checkMouse()
while not clicked:
    c1.move(1, 0)
    c2.move(1, 0)
    c3.move(1.5, 0)
    l1.move(1, 0)
    l2.move(1, 0)
    l3.move(1, 0)
    l4.move(1, 0)
    time.sleep(0.1)
    if color == 'white':
        color = 'black'
    else:
        color = 'white'
    c1.setFill(color)
    c2.setFill(color)

# wait until the user clics mouse then close win
win.getMouse()  # stop the presses!
win.close()  # this closes the window
print('Program is over !Goodbye')
