# Tree class
# Xu Song

from graphics import *


class Tree:
    def __init__(self, c, r):
        self.__row = r
        self.__col = c
        self.__location = Point(50 * c, 50 * r)
        self.__state = 'unburn'
        self.__nextState = 'lburn'

    def __str__(self):
        return str(self.__col) + ',' + str(self.__row)

    def __repr__(self):
        return self.__str__()

    def getcr(self):
        return self.__col, self.__row

    def getposition(self):
        return 50 * self.__col, 50 * self.__row

    def setstate(self):
        self.__state = self.__nextState
        if self.__nextState == 'lburn':
            self.__nextState = 'hburn'
        elif self.__nextState == 'hburn':
            self.__nextState = 'dead'
        elif self.__nextState == 'dead':
            self.__nextState = 'dead'

    def getstate(self):
        return self.__state

    def draw(self, win):
        if self.__state == 'lburn':
            treeImage = Image(Point(self.__col * 50, self.__row * 50), '2.png')
            treeImage.draw(win)
        elif self.__state == 'hburn':
            treeImage = Image(Point(self.__col * 50, self.__row * 50), '3.png')
            treeImage.draw(win)
        elif self.__state == 'dead':
            treeImage = Image(Point(self.__col * 50, self.__row * 50), '4.png')
            treeImage.draw(win)
        else:
            treeImage = Image(Point(self.__col * 50, self.__row * 50), '4.png')
            treeImage.draw(win)

    def checkstate(self):
        print(self.__state, self.__nextState)
