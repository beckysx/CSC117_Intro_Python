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

win.setCoords(0, 0, 100, 100)

# lines
xspan = 100  # think of this as "percent" not pixels
yspan = 100
border = 5  # the "extra" amount also contained in window
# The workspace is now from (0,0) to (100,100)
print(-border, -border, xspan + border, yspan + border)
win.setCoords(-border, -border, xspan + border, yspan + border)

print('Drawing horizontal gridlines')
for y in range(0, 101, 10):  # vertical lines
    print((0, y), (xspan, y))
    grid = Line(Point(0, y), Point(xspan, y))
    grid.setOutline('lightgray')
    grid.draw(win)

print('Click the workspace to get coordinates')
click = win.getMouse()  # get click Point
dot = Circle(click, 3)
dot.setFill('purple')
dot.draw(win)

x = click.getX()  # get X coordinate
y = click.getY()  # get Y coordinate
print('You clicked', (x, y))

# wait until the user clics mouse then close win
print('Click window anywhere to end')
win.getMouse()  # stop the presses!
win.close()  # this closes the window
print('Program is over !Goodbye')
