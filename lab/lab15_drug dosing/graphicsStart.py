# Example Code 
# CSC 117 F18
# Part of Solution to Lab 14: Functions 2
# Thomas E. Allen
#
# Note: I'm making this available especially for those who had
# difficulty with Lab 14.  It is not identical to the lab, but the
# functions initWindow, createButton, and clicked which may be helpful
# to you in future graphics labs.  Feel free to modify this (giving
# credit in your comments) or to use the functions that you wrote
# yourself.

from graphics import * # needed for all the graphics assignments
from random import randint # for the demo


def initWindow(title, width, height, xspan, yspan, border, grid):
    '''Creates a graphics window, initializes the coordinate system, and
    (optionally) draws a grid.

    Parameters
    ----------
    title : str
      The title of the window
    width : int
      Number of pixels across the window horizontally
    height : int
      Number of pixels down the window vertically
    xspan : float
    yspan : float
      Virtual number of pixels, with (0,0) in lower left corner
    grid : bool
      Set to True to draw a grid

    Output
    ------
    GraphWin
      The window created

    '''
    color = 'lightgreen' # feel free to mod this if you wish
    win = GraphWin(title, width, height)
    win.setCoords(-border, -border, xspan + border, yspan + border)
    if grid: # Gridlines for design and debugging
        for x in range(0, width, 10): # vertical lines
            vert = Line(Point(x, 0), Point(x, yspan))
            vert.setOutline(color) 
            vert.draw(win)
        for y in range(0, height, 10): # Horizontal lines 
            vert = Line(Point(0, y), Point(xspan, y))
            vert.setOutline(color) 
            vert.draw(win)
    return win


def createButton(win, x1, y1, x2, y2, bgColor,
                 caption, textSize, textColor):
    '''Creates a "button".  That is, it creates a Rectangle object bounded
by points (x1, y1) and displays that as a button for the user to
click.  It also displays a text label on top of the button (an Entry
object).  Returns both so that caller can detect clicks and modify the
button and/or label as needed.

    Parameters
    ----------
    win : GraphWin
      The window object
    x1, y1 : float
      Lower left corner of Rectangle (button)
    x2, y2 : float
      Upper right corner of Rectangle (button)
    bgColor : str
      background color of button (e.g., "red")
    caption : str
      text to display on top of button (e.g., "Click me!")
    textSize : int
      text point size
    textColor : str
      color of caption on top of button (e.g., "white")

    Output
    ------
    Rectangle
      The Graphics rectangle that we think of as the "button" itself
    Text
      The Graphics text box that we use to label the button

    '''
    button = Rectangle(Point(x1, y1), Point(x2, y2))
    button.setFill(bgColor)
    label = Text(button.getCenter(), caption)
    label.setOutline(textColor)
    label.setSize(textSize)
    button.draw(win)
    label.draw(win)
    return button, label

def clicked(button, aPoint):
    '''Returns true if aPoint is inside the Rectangle object button.  Usually the point will be obtained from a mouseclick, but it could be any point and any rectangle object.

    Parameters
    ----------
    button : Rectangle
      the bounds in which the point needs to be
    aPoint : Point
      the point that we want to check 

    Output
    ------
    bool
      True iff aPoint is in (or on) button

    '''
    p1 = button.getP1() # extract points
    p2 = button.getP2()
    x = aPoint.getX() # extract X and Y coords
    y = aPoint.getY()
    return (x >= p1.getX() and x <= p2.getX() and 
            y >= p1.getY() and y <= p2.getY())

# This is just for demo purposes
# This function gets a mouse click (Point) that is on the button
# It then undraws the button
def clickAway(button, label, win):
    clickPoint = win.getMouse()
    while not clicked(button, clickPoint):
        clickPoint = win.getMouse()
    label.undraw()
    button.undraw()

# This is just for demo purposes
# Think of it as the start of a whack-a-mole game ...
def main():
    win = initWindow('Stacks', 600, 600, 100, 100, 5, True)

    for i in range(10):
        x = randint(20, 80)
        y = randint(20, 80)
        button, label = createButton(win, x-10, y-10, x+10, y+10,
                                     'black', 'Hit me!', 20, 'white')
        clickAway(button, label, win)

    win.getMouse()
    win.close()
    
main()

