# Xu Song
# lab 12 The flight of the Gummy bear
# 24th Sep 2018
# partner: Madison Ebel
# Enter velocity 55 and angle 45 to win

from graphics import *
from math import sin, cos, pi

# Most of this first part is adapted from Lab 11 (the written guide)
print('Starting program.')

# Define the window object
print('Creating graphics window')
windowTitle = 'Text Entry Example'
windowWidth = 600  # width and height in pixels
windowHeight = 600
win = GraphWin(windowTitle, windowWidth, windowHeight)

# Rescale the window
print('Rescaling window to 100 x 100.')
xspan = 100  # now think of this as "percent" not pixels nec.
yspan = 100
border = 5  # the "extra" amount also contained in window
print('Screen range:', -border, -border, xspan + border, yspan + border)
win.setCoords(-border, -border, xspan + border, yspan + border)

# Draw grid lines for design and debugging
print('Drawing grid lines')
for x in range(0, windowWidth, 10):  # vertical lines
    vert = Line(Point(x, 0), Point(x, yspan))
    vert.setOutline('gray')
    vert.draw(win)
for y in range(0, windowHeight, 10):  # Horizontal lines
    vert = Line(Point(0, y), Point(xspan, y))
    vert.setOutline('gray')
    vert.draw(win)

# Draw a button on the screen
print('Draw button on screen.')
button = Rectangle(Point(80, 80), Point(100, 100))
buttonText = Text(Point(90, 90), 'Click me')
button.draw(win)
buttonText.draw(win)

# entry boxes for v & angle
angle = Entry(Point(23, 85), 5)
angle.draw(win)

v = Entry(Point(23, 95), 5)
v.draw(win)

angletext = Text(Point(10, 85), 'Enter angle:')
angletext.setSize(10)
angletext.draw(win)

vtext = Text(Point(10, 95), 'Enter velocity:')
vtext.setSize(10)
vtext.draw(win)

# Make user click button before continuing
# Pattern: Input validation loop
clickPoint = win.getMouse()  # get input
x = clickPoint.getX()  # extract X coordinate from Point object
y = clickPoint.getY()
_angle = angle.getText()  # also now get text
_v = v.getText()
while x < 80 or x > 100 or y < 80 or y > 100 or (_angle == "" and _v == ""):  # while input outside range
    # print('User clicked outside the box at x =', x, 'y =', y)
    clickPoint = win.getMouse()  # get input again
    x = clickPoint.getX()
    y = clickPoint.getY()
    _angle = angle.getText()  # also now get text
    _v = v.getText()
# print('User clicked inside the box at x =', x, 'y =', y)
button.setFill('lightblue')  # change box color just for fun

# get text from the entry box
r_angle = float(_angle)
print('You entered angle:', r_angle)
r_v = float(_v)
print('You entered velocity', r_v)

# draw launch pad
launch = Rectangle(Point(0, 0), Point(10, 10))
launch.draw(win)
launch.setFill('violet')

# draw target
target1 = Rectangle(Point(80, 0), Point(100, 20))
target1.draw(win)
target1.setFill('black')
target2 = Rectangle(Point(80, 20), Point(100, 25))
target2.draw(win)
target2.setFill('green')

# draw start point
startpoint = Point(5, 10)
startcircle = Circle(startpoint, 1.5)
startcircle.setFill('gray')
startcircle.draw(win)

# draw the parabola
parabolax = 5
parabolay = 10
t = 0
an = r_angle * (pi / 180)
ve = r_v
g = 32
parabolaPoint = Point(5, 10)

done = False

while not (done):
    ##parabolax>=0 and parabolax<=100 and parabolay>=10 and parabolay<=100:
    t += 0.05
    parabolax = 5 + (ve * cos(an)) * t
    parabolay = (-0.5 * g) * (t ** 2) + (ve * sin(an)) * t + 10
    parabolaPoint = Point(parabolax, parabolay)
    parabolaCircle = Circle(parabolaPoint, 1.5)
    parabolaCircle.setFill('gray')
    parabolaCircle.draw(win)

    # win text
    if 80 <= parabolax <= 100 and 23 <= parabolay <= 25:
        winText = Text(Point(50, 60), 'You Win!')
        winText.setSize(30)
        winText.draw(win)
        # if win,draw circles
        radius = 4
        for i in range(5):
            radius += 2
            wincirclePoint = Point(parabolax, parabolay)
            wincircle = Circle(wincirclePoint, radius)
            wincircle.setOutline('pink')
            wincircle.draw(win)
        done = True

    # lose text
    elif 0 > parabolax or 100 < parabolax or 0 > parabolay \
            or (80 <= parabolax <= 100 and 24 > parabolay):
        loseText = Text(Point(50, 60), 'You Lose!')
        loseText.setSize(30)
        loseText.draw(win)
        done = True

# Now if user clicks anywhere, program will terminate
print('Click graphics window anywhere to end program.')
win.getMouse()  # similar to input('Press ENTER to end')

print('Program ending.')
win.close()  # close graphics window
