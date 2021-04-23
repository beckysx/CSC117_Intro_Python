# Coin Lab
# Xu Song

from graphics import *


def window(winTile, winWidth, winHeight):
    win = GraphWin(winTile, winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)
    return win


def vertline(windowWidth, sep, winHeight, color, win):
    for x in range(0, windowWidth, sep):
        a = Line(Point(x, 0), Point(x, winHeight))
        a.setOutline(color)
        a.draw(win)


def horiline(windowWidth, sep, winHeight, color, win):
    for y in range(0, winHeight, sep):
        b = Line(Point(0, y), Point(windowWidth, y))
        b.setOutline(color)
        b.draw(win)


def drawCircle(x, y, win):
    cir = Circle(Point(x, y), 40)
    cir.draw(win)
    return cir


def getclick(win):
    clickPoint = win.getMouse()
    c = clickPoint.getX()
    d = clickPoint.getY()
    return c, d


def findex(a):
    if 0 < a < 80:
        f = 0
    elif 80 < a < 160:
        f = 1
    elif 160 < a < 240:
        f = 2
    elif 240 < a < 320:
        f = 3
    elif 320 < a < 400:
        f = 4
    elif 400 < a < 480:
        f = 5
    elif 480 < a < 560:
        f = 6
    elif 560 < a < 640:
        f = 7
    elif 640 < a < 720:
        f = 8
    elif 720 < a < 800:
        f = 9
    else:
        f = 0
    return f


def sindex(a):
    if 0 < a < 80:
        s = 0
    elif 80 < a < 160:
        s = 1
    elif 160 < a < 240:
        s = 2
    elif 240 < a < 320:
        s = 3
    elif 320 < a < 400:
        s = 4
    elif 400 < a < 480:
        s = 5
    elif 480 < a < 560:
        s = 6
    elif 560 < a < 640:
        s = 7
    elif 640 < a < 720:
        s = 8
    elif 720 < a < 800:
        s = 9
    else:
        s = 0
    return s


class Coin:
    def __init__(self, win, x, y):
        self.__win = win
        self.__front = Circle(Point(x, y), 40)
        self.__front.draw(win)
        self.__front.setFill('lightblue')
        self.__back = Circle(Point(x, y), 40)
        self.__frontup = True
        self.__x = x
        self.__y = y

    def __str__(self):
        return str(self.__x) + ',' + str(self.__y)

    def __repr__(self):
        return self.__str__()

    def flip(self, win):
        if self.__frontup:
            self.__frontup = False
            self.__front = drawCircle(self.__x, self.__y, win)
            self.__front.setFill('green')

        else:
            self.__frontup = True
            self.__back = drawCircle(self.__x, self.__y, win)
            self.__back.setFill('lightblue')


def main():
    game = True
    win = window('Coin', 800, 800)
    vertline(800, 80, 800, 'grey', win)
    horiline(800, 80, 800, 'grey', win)

    big = []
    for c in range(10):
        x = 80 * c + 40
        co = []
        for r in range(10):
            y = 80 * r + 40
            coin = Coin(win, x, y)
            co.append(coin)
        big.append(co)

    a, b = getclick(win)
    while game:
        f = findex(a)
        s = sindex(b)
        big[f][s].flip(win)
        a, b = getclick(win)


main()
