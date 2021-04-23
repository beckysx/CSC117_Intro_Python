# Xu Song
# Lab 14 Function 2
# 28th Sep 2018

from graphics import *
from math import sqrt


# STEP 1


def createButton(x1, y1, x2, y2, \
                 lableColor, lableText, textSize, textColor):
    rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
    text = Text(Point((x1 + x2) / 2, (y1 + y2) / 2), lableText)
    rectangle.setFill(lableColor)
    text.setSize(textSize)
    text.setTextColor(textColor)
    return rectangle, text


# STEP 2

def clicked(x1, y1, x2, y2, x, y):
    rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
    clickpoint = Point(x, y)
    done = True
    if x < x1 or x > x2 or y < y1 or y > y2:
        done = False
    return done


# STEP 3

def distance(x1, x2, y1, y2):
    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d


# STEP 4

def circleClicked(centerpointX, centerpointY, x2, y2, radius, d):
    circle = Circle(Point(centerpointX, centerpointY), radius)
    clickpoint = Point(x2, y2)
    d = sqrt((x2 - centerpointX) ** 2 + (y2 - centerpointY) ** 2)
    test = True
    if abs(d) > radius:
        test = False
    return test


def main():
    # step1
    win = GraphWin('Lab 14', 600, 600)
    rectangle, text = createButton(175, 200, 375, 400, 'green', 'Click Me', 30, 'black')
    rectangle.draw(win)
    text.draw(win)

    # step2
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    while not clicked(175, 200, 375, 400, x, y):
        clickPoint = win.getMouse()
        x = clickPoint.getX()
        y = clickPoint.getY()
    if clicked(175, 200, 375, 400, x, y):
        rectangle.setFill('red')

    # step3
    clickPoint1 = win.getMouse()
    x1 = clickPoint1.getX()
    y1 = clickPoint1.getY()
    # draw point
    clickPoint1.draw(win)

    clickPoint2 = win.getMouse()
    x2 = clickPoint2.getX()
    y2 = clickPoint2.getY()
    # draw point
    clickPoint2.draw(win)

    # draw line
    line = Line(clickPoint1, clickPoint2)
    line.draw(win)

    # calculate and display distance
    d = distance(x1, x2, y1, y2)
    dtext = Text(Point((x1 + x2) / 2 + 20, (y1 + y2) / 2), '%.2f' % d)
    dtext.setSize(10)
    dtext.draw(win)

    # step4
    circle = Circle(Point(275, 500), 60)
    circle.setFill('blue')
    circle.draw(win)
    clickPoint3 = win.getMouse()
    x3 = clickPoint3.getX()
    y3 = clickPoint3.getY()
    d = distance(x3, 275, y3, 500)
    while not circleClicked(275, 500, x3, y3, 60, d):
        clickPoint3 = win.getMouse()
        x3 = clickPoint3.getX()
        y3 = clickPoint3.getY()
    if circleClicked(275, 500, x3, y3, 60, d):
        circle.setFill('red')

    # close window
    win.getMouse()
    win.close()


main()
