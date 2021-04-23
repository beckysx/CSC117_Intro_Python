# Xu Song
# Mastermind

import random
from graphics import *
from math import sqrt


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


def click(win):
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    return x, y


def bluebutton_click(x, y):
    d = sqrt((x - 550) ** 2 + (y - 80) ** 2)
    test = True
    color = 'lightblue'
    if abs(d) > 20:
        test = False
    return test, color


def greenbutton_click(x, y):
    d = sqrt((x - 550) ** 2 + (y - 160) ** 2)
    test = True
    color = 'green'
    if abs(d) > 20:
        test = False
    return test, color


def pinkbutton_click(x, y):
    d = sqrt((x - 550) ** 2 + (y - 240) ** 2)
    test = True
    color = 'pink'
    if abs(d) > 20:
        test = False
    return test, color


def purplebutton_click(x, y):
    d = sqrt((x - 550) ** 2 + (y - 320) ** 2)
    test = True
    color = 'purple'
    if abs(d) > 20:
        test = False
    return test, color


def redbutton_click(x, y):
    d = sqrt((x - 550) ** 2 + (y - 400) ** 2)
    test = True
    color = 'red'
    if abs(d) > 20:
        test = False
    return test, color


def orangebutton_click(x, y):
    d = sqrt((x - 550) ** 2 + (y - 480) ** 2)
    test = True
    color = 'orange'
    if abs(d) > 20:
        test = False
    return test, color


def start_button(x, y):
    done = True
    if x < 500 or x > 700 or y < 540 or y > 590:
        done = False
    return done


def quit_button(x, y):
    500, 600, 700, 650
    done = True
    if x < 500 or x > 700 or y < 600 or y > 650:
        done = False
    return done


def undrawthings(name):
    name.undraw()


def colorthecirle(win, x, y, color):
    cir = drawCircle(x, y, 20, win)
    cir.setFill(color)


def whitepeg(x, y, win):
    cir = drawCircle(x, y, 5, win)


def blackpeg(x, y, win):
    cir = drawCircle(x, y, 5, win)
    cir.setFill('black')


def rightColor():
    color1 = random.choice(['red', 'green', 'lightblue', 'purple', 'pink', 'orange'])
    color2 = random.choice(['red', 'green', 'lightblue', 'purple', 'pink', 'orange'])
    color3 = random.choice(['red', 'green', 'lightblue', 'purple', 'pink', 'orange'])
    color4 = random.choice(['red', 'green', 'lightblue', 'purple', 'pink', 'orange'])
    return color1, color2, color3, color4


def main():
    # draw a window
    win = window('Mastermind', 800, 700)

    # draw game on window
    rec = drawRectangle(50, 50, 450, 650, win)
    line_y = 110
    for seperate in range(8):
        line = drawLine(50, line_y, 450, line_y, win)
        line_y += 60

    guessCircle_y = 80
    for guessCircle_inlne in range(8):
        cir = drawCircle(225, guessCircle_y, 20, win)
        guessCircle_y += 60

    guessCircle_y = 80
    for guessCircle_inlne in range(8):
        cir = drawCircle(285, guessCircle_y, 20, win)
        guessCircle_y += 60

    guessCircle_y = 80
    for guessCircle_inlne in range(8):
        drawCircle(345, guessCircle_y, 20, win)
        guessCircle_y += 60

    guessCircle_y = 80
    for guessCircle_inlne in range(8):
        cir = drawCircle(405, guessCircle_y, 20, win)
        guessCircle_y += 60

    rightCircle_x = 225
    for rightCircle_inrow in range(4):
        cir = drawCircle(rightCircle_x, 590, 20, win)
        rightCircle_x += 60

    button_x = 550
    buttontext_x = 650
    size = 20
    bluebutton = drawCircle(button_x, 80, 30, win)
    bluebutton.setFill('lightblue')
    textinfo('Blue', buttontext_x, 80, size, win)

    greenbutton = drawCircle(button_x, 160, 30, win)
    greenbutton.setFill('green')
    textinfo('Greeen', buttontext_x, 160, size, win)

    pinkbutton = drawCircle(button_x, 240, 30, win)
    pinkbutton.setFill('pink')
    textinfo('Pink', buttontext_x, 240, size, win)

    purplebutton = drawCircle(button_x, 320, 30, win)
    purplebutton.setFill('purple')
    textinfo('Purple', buttontext_x, 320, size, win)

    redbutton = drawCircle(button_x, 400, 30, win)
    redbutton.setFill('red')
    textinfo('Red', buttontext_x, 400, size, win)

    orangebutton = drawCircle(button_x, 480, 30, win)
    orangebutton.setFill('orange')
    textinfo('Orange', buttontext_x, 480, size, win)

    start_button_rec = drawRectangle(500, 540, 700, 590, win)
    start_info = textinfo('Start', 600, 565, 20, win)
    quit_button_rec = drawRectangle(500, 600, 700, 650, win)
    quit_info = textinfo('Quit', 600, 625, 20, win)

    x, y = click(win)
    start = start_button(x, y)
    q = quit_button(x, y)
    while start:

        c1, c2, c3, c4 = rightColor()
        start = False
        undrawthings(start_button_rec)
        undrawthings(start_info)
        undrawthings(quit_button_rec)
        undrawthings(quit_info)
        count = 0
        test = True
        guesscircle_y = 80
        print('Click Color Buttons on the Screen, Please.')

        while count <= 7 and test:
            blackpeg_num = 0
            whitepeg_num = 0
            guesscircle_x = 225
            peg_x = 60
            for guess in range(4):
                guess_x, guess_y = click(win)
                blue_test, blue = bluebutton_click(guess_x, guess_y)
                green_test, green = greenbutton_click(guess_x, guess_y)
                orange_test, orange = orangebutton_click(guess_x, guess_y)
                pink_test, pink = pinkbutton_click(guess_x, guess_y)
                purple_test, purple = purplebutton_click(guess_x, guess_y)
                red_test, red = redbutton_click(guess_x, guess_y)
                if blue_test:
                    colorthecirle(win, guesscircle_x, guesscircle_y, blue)
                    guesscolor = blue
                if green_test:
                    colorthecirle(win, guesscircle_x, guesscircle_y, green)
                    guesscolor = green
                if orange_test:
                    colorthecirle(win, guesscircle_x, guesscircle_y, orange)
                    guesscolor = orange
                if pink_test:
                    colorthecirle(win, guesscircle_x, guesscircle_y, pink)
                    guesscolor = pink
                if purple_test:
                    colorthecirle(win, guesscircle_x, guesscircle_y, purple)
                    guesscolor = purple
                if red_test:
                    colorthecirle(win, guesscircle_x, guesscircle_y, red)
                    guesscolor = red

                if c1 == guesscolor:
                    whitepeg_num += 1
                elif c2 == guesscolor:
                    whitepeg_num += 1
                elif c3 == guesscolor:
                    whitepeg_num += 1
                elif c4 == guesscolor:
                    whitepeg_num += 1

                if guess == 0 and c1 == guesscolor:
                    blackpeg_num += 1
                    whitepeg_num -= 1

                elif guess == 1 and c2 == guesscolor:
                    blackpeg_num += 1
                    whitepeg_num -= 1


                elif guess == 2 and c3 == guesscolor:
                    blackpeg_num += 1
                    whitepeg_num -= 1


                elif guess == 3 and c4 == guesscolor:
                    blackpeg_num += 1
                    whitepeg_num -= 1

                guesscircle_x += 60

            for pegdraw in range(whitepeg_num):
                whitepeg(peg_x, guesscircle_y, win)
                peg_x += 15

            for pegdraw in range(whitepeg_num):
                blackpeg(peg_x, guesscircle_y, win)
                peg_x += 15

            if blackpeg_num == 4:
                colorthecirle(win, 225, 590, c1)
                colorthecirle(win, 285, 590, c2)
                colorthecirle(win, 345, 590, c3)
                colorthecirle(win, 405, 590, c4)
                for pegdraw in range(4):
                    blackpeg(peg_x, guesscircle_y, win)
                    peg_x += 15
                print('You WIN!!!')
                test = False

            count += 1
            guesscircle_y += 60

            if count == 8 and test:
                colorthecirle(win, 225, 590, c1)
                colorthecirle(win, 285, 590, c2)
                colorthecirle(win, 345, 590, c3)
                colorthecirle(win, 405, 590, c4)
                print('You LOSE!!!')

        start_button_rec = drawRectangle(500, 540, 700, 590, win)
        start_info = textinfo('Start', 600, 565, 20, win)
        quit_button_rec = drawRectangle(500, 600, 700, 650, win)
        quit_info = textinfo('Quit', 600, 625, 20, win)
        x, y = click(win)
        start = start_button(x, y)

        rerec1_y1 = 50
        rerec1_y2 = 110
        for rerec1 in range(8):
            rec = drawRectangle(50, rerec1_y1, 450, rerec1_y2, win)
            rec.setFill('white')
            rerec1_y1 += 60
            rerec1_y2 += 60

        rerec2 = drawRectangle(50, 530, 450, 650, win)
        rerec2.setFill('white')

        guessCircle_y = 80
        for guessCircle_inlne in range(8):
            cir = drawCircle(225, guessCircle_y, 20, win)
            guessCircle_y += 60

        guessCircle_y = 80
        for guessCircle_inlne in range(8):
            cir = drawCircle(285, guessCircle_y, 20, win)
            guessCircle_y += 60

        guessCircle_y = 80
        for guessCircle_inlne in range(8):
            drawCircle(345, guessCircle_y, 20, win)
            guessCircle_y += 60

        guessCircle_y = 80
        for guessCircle_inlne in range(8):
            cir = drawCircle(405, guessCircle_y, 20, win)
            guessCircle_y += 60

        rightCircle_x = 225
        for rightCircle_inrow in range(4):
            cir = drawCircle(rightCircle_x, 590, 20, win)
            rightCircle_x += 60

        rightCircle_x = 225
        for rightCircle_inrow in range(4):
            cir = drawCircle(rightCircle_x, 590, 20, win)
            rightCircle_x += 60

        q = quit_button(x, y)
        if q:
            win.close()

    if q:
        win.close()


main()
