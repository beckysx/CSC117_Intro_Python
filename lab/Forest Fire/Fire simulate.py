# Forest Fire
# Xu Song
from typing import List
from Tree import *
import time
import random


def window(winTile, winWidth, winHeight):
    win = GraphWin(winTile, winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)
    return win


def drawRectangle(x1, y1, x2, y2, win):
    rec = Rectangle(Point(x1, y1), Point(x2, y2))
    rec.draw(win)
    return rec


def entryBox(x1, y1, length, win):
    box = Entry(Point(x1, y1), length)
    box.draw(win)
    return box


def textInfo(massage, x1, y1, size, win, color):
    textinfo = Text(Point(x1, y1), massage)
    textinfo.setSize(size)
    textinfo.setTextColor(color)
    textinfo.draw(win)
    return textinfo


def click(win):
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    return x, y


def ignite(probability):
    burn = False
    a = random.randint(1, 100)
    if a <= (probability * 100):
        burn = True
    return burn


def find_in2(y):
    if 25 < y < 75:
        in2 = 0
    elif 75 < y < 125:
        in2 = 1
    elif 125 < y < 175:
        in2 = 2
    elif 175 < y < 225:
        in2 = 3
    elif 225 < y < 275:
        in2 = 4
    elif 275 < y < 325:
        in2 = 5
    elif 325 < y < 375:
        in2 = 6
    elif 375 < y < 425:
        in2 = 7
    elif 425 < y < 475:
        in2 = 8
    elif 475 < y < 525:
        in2 = 9
    return in2


def find_in1(x):
    if 25 < x < 75:
        in1 = 0
    elif 75 < x < 125:
        in1 = 1
    elif 125 < x < 175:
        in1 = 2
    elif 175 < x < 225:
        in1 = 3
    elif 225 < x < 275:
        in1 = 4
    elif 275 < x < 325:
        in1 = 5
    elif 325 < x < 375:
        in1 = 6
    elif 375 < x < 425:
        in1 = 7
    elif 425 < x < 475:
        in1 = 8
    elif 475 < x < 525:
        in1 = 9
    return in1


def main():
    # draw window and buttons
    win = window('Forest Fire', 800, 650)
    probText = textInfo('Probability of Spreading', 650, 400, 15, win, 'black')
    hintText = textInfo('Enter 0 to 1(e.g. 0.25)', 650, 380, 15, win, 'black')
    probBox = entryBox(650, 350, 15, win)
    regrowButton = drawRectangle(580, 230, 720, 270, win)
    regrowText = textInfo('Regrow the Forest', 650, 250, 15, win, 'black')
    existButton = drawRectangle(580, 100, 720, 140, win)
    existText = textInfo('Exist', 650, 120, 15, win, 'black')

    # draw the forest and create 2d list
    forest = []
    for c in range(1, 11):
        column = []
        for r in range(1, 11):
            treeImage = Image(Point(c * 50, r * 50), '1.png')
            treeImage.draw(win)
            tree = Tree(c, r)
            column.append(tree)
        forest.append(column)

    game = True

    while game:

        x, y = click(win)  # getclick
        _prob = probBox.getText()  # get text from the entry box

        while _prob == '':
            x, y = click(win)  # getclick
            _prob = probBox.getText()  # get text from the entry box

        prob = float(_prob)  # convert prob to float

        #  find the start tree position
        in2 = find_in2(y)
        in1 = find_in1(x)

        forest[in1][in2].setstate()
        forest[in1][in2].draw(win)  # the first tree start burning

        stop = False
        while not stop:  # the fire won't stop untill no tree is on fire
            for index in range(len(forest)):
                for trees in forest[index]:  # check every tree in 2d list
                    state = trees.getstate()
                    if state == 'lburn' or state == 'hburn':  # any tree on fire change to nextstate
                        trees.setstate()
                        trees.draw(win)
                    if state == 'unburn':
                        # find 2d list indexes to specify tree's position
                        x, y = trees.getposition()
                        c, r = trees.getcr()
                        in2 = find_in2(y)
                        in1 = find_in1(x)
                        burn_chance = False
                        # find trees' positions on four directions
                        if c == 1 and 2 <= r <= 9:  # no west trees
                            eT = forest[in1 + 1][in2]
                            nT = forest[in1][in2 + 1]
                            sT = forest[in1][in2 - 1]
                            # check tree state around the tree
                            eTs = eT.getstate()
                            nTs = nT.getstate()
                            sTs = sT.getstate()
                            if eTs == 'lburn' or nTs == 'lburn' or sTs == 'lburn' or \
                                    eTs == 'hburn' or nTs == 'hburn' or sTs == 'hburn':
                                burn_chance = True
                                # print('yes')
                            # find out if the tree will burn
                            if burn_chance:
                                burn = ignite(prob)
                                if burn:
                                    trees.setstate()
                                    trees.draw(win)
                        elif c == 10 and 2 <= r <= 9:  # no east trees
                            wT = forest[in1 - 1][in2]
                            nT = forest[in1][in2 + 1]
                            sT = forest[in1][in2 - 1]
                            # check tree state around the tree
                            wTs = wT.getstate()
                            nTs = nT.getstate()
                            sTs = sT.getstate()
                            if wTs == 'lburn' or nTs == 'lburn' or sTs == 'lburn' or \
                                    wTs == 'hburn' or nTs == 'hburn' or sTs == 'hburn':
                                burn_chance = True
                            # find out if the tree will burn
                            if burn_chance:
                                burn = ignite(prob)
                                if burn:
                                    trees.setstate()
                                    trees.draw(win)
                        elif r == 1 and 2 <= c <= 9:  # no south trees
                            eT = forest[in1 + 1][in2]
                            wT = forest[in1 - 1][in2]
                            nT = forest[in1][in2 + 1]
                            # check tree state around the tree
                            eTs = eT.getstate()
                            wTs = wT.getstate()
                            nTs = nT.getstate()
                            if eTs == 'lburn' or wTs == 'lburn' or nTs == 'lburn' or \
                                    eTs == 'hburn' or wTs == 'hburn' or nTs == 'hburn':
                                burn_chance = True
                            # find out if the tree will burn
                            if burn_chance:
                                burn = ignite(prob)
                                if burn:
                                    trees.setstate()
                                    trees.draw(win)
                        elif r == 10 and 2 <= c <= 9:  # no north trees
                            eT = forest[in1 + 1][in2]
                            wT = forest[in1 - 1][in2]
                            sT = forest[in1][in2 - 1]
                            # check tree state around the tree
                            eTs = eT.getstate()
                            wTs = wT.getstate()
                            sTs = sT.getstate()
                            if eTs == 'lburn' or wTs == 'lburn' or sTs == 'lburn' or \
                                    eTs == 'hburn' or wTs == 'hburn' or sTs == 'hburn':
                                burn_chance = True
                            # find out if the tree will burn
                            if burn_chance:
                                burn = ignite(prob)
                                if burn:
                                    trees.setstate()
                                    trees.draw(win)
                        elif r == 1 and c == 1:  # no west and south trees
                            eT = forest[in1 + 1][in2]
                            nT = forest[in1][in2 + 1]
                            # check tree state around the tree
                            eTs = eT.getstate()
                            nTs = nT.getstate()
                            if eTs == 'lburn' or nTs == 'lburn' or eTs == 'hburn' or nTs == 'hburn':
                                burn_chance = True
                            # find out if the tree will burn
                            if burn_chance:
                                burn = ignite(prob)
                                if burn:
                                    trees.setstate()
                                    trees.draw(win)
                        elif r == 1 and c == 10:  # no east and south trees
                            wT = forest[in1 - 1][in2]
                            nT = forest[in1][in2 + 1]
                            # check tree state around the tree
                            wTs = wT.getstate()
                            nTs = nT.getstate()
                            if wTs == 'lburn' or nTs == 'lburn' or wTs == 'hburn' or nTs == 'hburn':
                                burn_chance = True
                            # find out if the tree will burn
                            if burn_chance:
                                burn = ignite(prob)
                                if burn:
                                    trees.setstate()
                                    trees.draw(win)
                        elif r == 10 and c == 1:  # no north and west trees
                            eT = forest[in1 + 1][in2]
                            sT = forest[in1][in2 - 1]
                            # check tree state around the tree
                            eTs = eT.getstate()
                            sTs = sT.getstate()
                            if eTs == 'lburn' or sTs == 'lburn' or eTs == 'hburn' or sTs == 'hburn':
                                burn_chance = True
                            # find out if the tree will burn
                            if burn_chance:
                                burn = ignite(prob)
                                if burn:
                                    trees.setstate()
                                    trees.draw(win)
                        elif r == 10 and c == 10:  # no north and east trees
                            wT = forest[in1 - 1][in2]
                            sT = forest[in1][in2 - 1]
                            # check tree state around the tree
                            wTs = wT.getstate()
                            sTs = sT.getstate()
                            if wTs == 'lburn' or sTs == 'lburn' or wTs == 'hburn' or sTs == 'hburn':
                                burn_chance = True
                            # find out if the tree will burn
                            if burn_chance:
                                burn = ignite(prob)
                                if burn:
                                    trees.setstate()
                                    trees.draw(win)
                        else:
                            eT = forest[in1 + 1][in2]
                            wT = forest[in1 - 1][in2]
                            nT = forest[in1][in2 + 1]
                            sT = forest[in1][in2 - 1]
                            # check tree state around the tree
                            eTs = eT.getstate()
                            wTs = wT.getstate()
                            nTs = nT.getstate()
                            sTs = sT.getstate()
                            if eTs == 'lburn' or wTs == 'lburn' or nTs == 'lburn' or sTs == 'lburn' or \
                                    eTs == 'hburn' or wTs == 'hburn' or nTs == 'hburn' or sTs == 'hburn':
                                burn_chance = True
                            # find out if the tree will burn
                            if burn_chance:
                                burn = ignite(prob)
                                if burn:
                                    trees.setstate()
                                    trees.draw(win)
            time.sleep(1.5)
            # make sure the forest only contains deadtree and unburn tree
            treestates = []
            for index in range(len(forest)):
                for trees in forest[index]:  # check every tree in 2d list
                    state = trees.getstate()
                    treestates.append(state)
            if ('lburn' not in treestates) and ('hburn' not in treestates):
                stop = True

        # calculate how many trees are dead
        deadtree = 0
        treestates = []
        for index in range(len(forest)):
            for trees in forest[index]:  # check every tree in 2d list
                state = trees.getstate()
                treestates.append(state)
        for states in treestates:
            if states == 'dead':
                deadtree += 1
        # print the result text
        sumtext = textInfo(str(deadtree) + '% of the forest burned out.', 400, 600, 30, win, 'red')

        # check if click re-grow button or exist button
        x, y = click(win)  # getclick

        # exist button click
        if 580 <= x <= 720 and 100 <= y <= 140:
            win.close()
            game = False

        # re-grow button clicked
        else:
            sumtext.undraw()
            _prob = probBox.getText()  # get text from the entry box
            # new forest
            forest: List[List[Tree]] = []
            for c in range(1, 11):
                column = []
                for r in range(1, 11):
                    treeImage = Image(Point(c * 50, r * 50), '1.png')
                    treeImage.draw(win)
                    tree = Tree(c, r)
                    column.append(tree)
                forest.append(column)


main()
