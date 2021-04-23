# Xu Song
# Hangman
# 22nd Oct

import random
from graphics import *


def window(winTile, winWidth, winHeight):
    win = GraphWin(winTile, winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)
    return win


def drawRectangle(x1, y1, x2, y2, win):
    rec = Rectangle(Point(x1, y1), Point(x2, y2))
    rec.draw(win)
    return rec


def drawCircle(x, y, radius, win):
    cir = Circle(Point(x, y), radius)
    cir.draw(win)
    return cir


def drawLine(x1, y1, x2, y2, win):
    line = Line(Point(x1, y1), Point(x2, y2))
    line.draw(win)
    return line


def textinfo(massage, x1, y1, size, win):
    textinfo = Text(Point(x1, y1), massage)
    textinfo.setSize(size)
    textinfo.draw(win)
    return textinfo


def entryBox(x1, y1, length, win):
    box = Entry(Point(x1, y1), length)
    box.draw(win)
    return box


def click(win):
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    return x, y


def readfile(filename):
    file = open(filename, 'r')
    line = file.readline()
    wordlist = []
    while line != '':
        line = line.rstrip('\n')
        wordlist.append(line)
        line = file.readline()
    return wordlist


def submitbuttonGet(win, button):
    x, y = click(win)
    while x < 200 or x > 260 or y < 190 or y > 210:
        x, y = click(win)
    letter = button.getText()
    return letter


def main():
    # build a window
    win = window('Hangman', 600, 400)

    # draw a shelf
    drawLine(500, 20, 600, 20, win)
    drawLine(550, 20, 550, 250, win)
    drawLine(550, 250, 500, 250, win)
    drawLine(500, 250, 500, 220, win)

    # draw entrybox
    box = entryBox(150, 200, 5, win)
    box_text = textinfo('Guess: ', 100, 200, 10, win)
    submitButton = drawRectangle(260, 190, 200, 210, win)
    textinfo('Submit', 230, 200, 10, win)

    # draw the alphabet
    alrec = drawRectangle(35, 130, 440, 150, win)
    num_x = 50
    for num in range(97, 123):
        letter = chr(num)
        alphabet = textinfo(letter, num_x, 140, 12, win)
        num_x += 15

    # randomly choose a word from list
    wordlist = readfile('puzzles.txt')
    chosen = random.choice(wordlist)
    letterline = 0
    for letter in chosen:
        letterline += 1

    letterline_y = 300
    letterline_x = 50
    for line in range(letterline):
        drawLine(letterline_x, letterline_y, letterline_x + 30, letterline_y, win)
        letterline_x += 50

    guess = True
    wrong = 0
    right = 0
    guessLetter = submitbuttonGet(win, box)
    dontshow = []
    dontshow.append(ord(guessLetter))
    submitButton.setFill('lightblue')
    while guess:
        index = 0
        letterline_x = 50
        letterwritten_y = 310
        for letter in chosen:
            index += 1
            letterline_x = index * 50
            letterwritten_x = letterline_x + 15
            if guessLetter == letter:
                textinfo(letter, letterwritten_x, letterwritten_y, 15, win)
                right += 1
        if guessLetter not in chosen:
            wrong += 1
        if wrong == 1:
            drawCircle(500, 210, 10, win)
        if wrong == 2:
            drawLine(500, 200, 500, 150, win)
        if wrong == 3:
            drawLine(500, 200, 485, 175, win)
        if wrong == 4:
            drawLine(500, 200, 525, 175, win)
        if wrong == 5:
            guess = False
            oseinfo = textinfo('Lose!', 500, 300, 20, win)
            loseinfo.setTextColor('red')
        if right == letterline:
            guess = False
            wininfo = textinfo('Win!', 500, 300, 20, win)
            wininfo.setTextColor('blue')
        submitButton.setFill('white')
        alrec = drawRectangle(35, 130, 440, 150, win)
        alrec.setFill('white')
        num_x = 50
        for num in range(97, 123):
            letter = chr(num)
            alphabet = textinfo(letter, num_x, 140, 12, win)
            if num in dontshow:
                alphabet.undraw()
            num_x += 15
        guessLetter = submitbuttonGet(win, box)
        dontshow.append(ord(guessLetter))
        print(dontshow)
        submitButton.setFill('lightblue')


main()
