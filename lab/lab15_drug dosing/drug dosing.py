# Lab 15 Drug Dosing
# Xu Song

from graphics import *


def window(winTile, winWidth, winHeight):
    win = GraphWin(winTile, winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)
    return win


def drawLine(x1, y1, x2, y2, color, win):
    line = Line(Point(x1, y1), Point(x2, y2))
    line.setOutline(color)
    line.draw(win)
    return line


def drawRectangle(x1, y1, x2, y2, win):
    rec = Rectangle(Point(x1, y1), Point(x2, y2))
    rec.draw(win)
    return rec


def entryBox(x1, y1, length, win):
    box = Entry(Point(x1, y1), length)
    box.draw(win)
    return box


def textinfo(massage, x1, y1, size, win, color):
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


def main():
    # draw a window
    win = window('Drug Dosage Simulator', 1200, 700)

    # ask for decay rate
    decay_r_box = entryBox(1050, 85, 10, win)
    decay_r_text = textinfo('Enter decay rate:', 950, 85, 12, win, 'black')

    # start button
    startButton = drawRectangle(200, 250, 600, 550, win)
    startButton_text = textinfo('Click to Start the Program', 400, 400, 30, win, 'black')
    startButton.setFill('lightblue')
    x1, y1 = click(win)

    # get textfrom entry box
    decay_r_get = decay_r_box.getText()

    # transfer to float
    dr = float(decay_r_get)

    while x1 < 400 or x1 > 800 or y1 < 200 or y1 > 500 or decay_r_get == "" or dr >= 1:
        x1, y1 = click(win)
        decay_r_get = decay_r_box.getText()
        dr = float(decay_r_get)

    startButton.undraw()
    startButton_text.undraw()

    # draw main part of the project
    line = drawLine(10, 120, 1190, 120, 'black', win)
    dosageinfo_text = textinfo('Dosage(mg every 8 hours)', 130, 535, 15, win, 'black')
    graph = drawRectangle(500, 250, 1050, 600, win)
    deathinfo = drawRectangle(10, 10, 800, 90, win)
    dosagebutton = drawRectangle(900, 10, 1150, 50, win)
    dosagebutton.setFill('lightblue')
    dosagebutton_text = textinfo('Try Next Dosage', 1025, 30, 15, win, 'black')

    # draw x-axis & y-axis of the graph
    hour_text = textinfo('Hour', 775, 200, 20, win, 'black')
    xAxis_x = 500
    xAxis_num = 0
    for x_axis in range(22):
        xAxis_num_tran = str(xAxis_num)
        x_axis_info = textinfo(xAxis_num_tran, xAxis_x, 230, 10, win, 'black')
        xAxis_num += 8
        xAxis_x += 25

    druginbody_text = textinfo('Drug in body(mg)', 500, 630, 20, win, 'black')
    yAxis_y = 250
    yAxis_num = 0
    for y_axis in range(11):
        yAxis_num_tran = str(yAxis_num)
        y_axis_info = textinfo(yAxis_num_tran, 480, yAxis_y, 10, win, 'black')
        yAxis_num += 10
        yAxis_y += 25

    # ask for vlues
    instruction_text = textinfo('Enter values on shell', 775, 425, 20, win, 'red')

    # verify effective value
    effective_value = float(input('Effective value: '))
    while effective_value < 0 or effective_value > 100:
        print('Invalid value! The effective value should greater than 0 and smaller than 100.')
        effective_value = float(input('Effective value:'))

    # verify overdose value
    overdose_value = float(input('Overdose value: '))
    while overdose_value < 0 or overdose_value > 100 or overdose_value <= effective_value:
        print('Invalid value! The overdose value should greater than effective value \
and greater than 0 and smaller than 100')
        overdose_value = float(input('Overdose value:'))

    # verify lethal value
    lethal_value = float(input('Enter lethal value: '))
    while lethal_value < 0 or lethal_value > 100 or lethal_value <= overdose_value:
        print('Invalid value! The lethal value should greater than overdose value \
and greater than 0 and smaller than 100')
        lethal_value = float(input('Enter lethal value: '))

    # undraw the instruction
    instruction_text.undraw()

    # draw line on graph
    effective_line = drawLine(500, 250 + 2.5 * effective_value, 1050, 250 + 2.5 * effective_value, 'green', win)
    overdose_line = drawLine(500, 250 + 2.5 * overdose_value, 1050, 250 + 2.5 * overdose_value, 'orange', win)
    lethal_line = drawLine(500, 250 + 2.5 * lethal_value, 1050, 250 + 2.5 * lethal_value, 'red', win)

    # line explain
    effective_text = textinfo('Effective', 1100, 250 + 2.5 * effective_value, 12, win, 'green')
    overdose_text = textinfo('Overdose', 1100, 250 + 2.5 * overdose_value, 12, win, 'orange')
    lethal_text = textinfo('Lethal', 1100, 250 + 2.5 * lethal_value, 12, win, 'red')

    instruction_text2 = textinfo("Click 'Try Next Dosage' button", 775, 150, 20, win, 'red')

    clickpoint = False
    x2, y2 = click(win)
    dose = 0
    dosagebox_text_y = 500
    deathinfo_text = textinfo('  ', 400, 50, 15, win, 'black')
    drug_in_blood_c = 0
    if 900 <= x2 <= 1150 and 10 <= y2 <= 50:
        clickpoint = True
    while not clickpoint:
        x2, y2 = click(win)
        if 900 <= x2 <= 1150 and 10 <= y2 <= 50:
            clickpoint = True

    if clickpoint:
        instruction_text2.undraw()

    while clickpoint and dose < 10 and drug_in_blood_c < 250 + 2.5 * lethal_value:
        dose += 1
        # redraw graph
        graph = drawRectangle(500, 250, 1050, 600, win)
        graph.setFill('white')
        # redraw lines
        effective_line = drawLine(500, 250 + 2.5 * effective_value, 1050, 250 + 2.5 * effective_value, 'green', win)
        overdose_line = drawLine(500, 250 + 2.5 * overdose_value, 1050, 250 + 2.5 * overdose_value, 'orange', win)
        lethal_line = drawLine(500, 250 + 2.5 * lethal_value, 1050, 250 + 2.5 * lethal_value, 'red', win)
        # rewrite death info
        deathinfo_text.undraw()

        drug_in_blood_p = 0
        time = 500
        drug_in_blood_c = 250 + drug_in_blood_p * (1 - dr) + dose
        effective_hour = 200
        overdose_hour = 200
        lethal_hour = 200
        while drug_in_blood_c < 250 + 2.5 * lethal_value and time < 1025:
            time += 25
            drug_in_blood_p += dose
            drug_in_blood_c = 250 + drug_in_blood_p * (1 - dr) + dose
            drug_in_blood_line = drawLine(time, 250, time, drug_in_blood_c, 'black', win)
            if drug_in_blood_c >= 250 + 2.5 * effective_value and drug_in_blood_c < 250 + 2.5 * overdose_value \
                    and effective_hour > ((time - 500) // 25) * 8:
                effective_hour = ((time - 500) // 25) * 8
            if drug_in_blood_c >= 250 + 2.5 * overdose_value and drug_in_blood_c < 250 + 2.5 * lethal_value \
                    and overdose_hour > ((time - 500) // 25) * 8:
                overdose_hour = ((time - 500) // 25) * 8
            if drug_in_blood_c >= 250 + 2.5 * lethal_value and lethal_hour > ((time - 500) // 25) * 8:
                lethal_hour = ((time - 500) // 25) * 8

        if drug_in_blood_c < 250 + 2.5 * effective_value:
            dosagebox_text = textinfo(str(dose) + ':Ineffective(never enough drug in the body)', 215, \
                                      dosagebox_text_y, 12, win, 'black')
            deathinfo_text = textinfo('With a dose of ' + str(dose) + ' mg every 8 hours,nothing happened', 400, 50, 15,
                                      win, 'black')

        if drug_in_blood_c >= 250 + 2.5 * effective_value and drug_in_blood_c < 250 + 2.5 * overdose_value:
            dosagebox_text = textinfo(str(dose) + ':Effective beginning at hour' + str(effective_hour) \
                                      , 215, dosagebox_text_y, 12, win, 'green')
            deathinfo_text = textinfo(
                'With a dose of ' + str(dose) + ' mg every 8 hours the patient had effective dose at hour ' \
                + str(effective_hour), 400, 50, 15, win, 'black')

        if drug_in_blood_c >= 250 + 2.5 * overdose_value and drug_in_blood_c < 250 + 2.5 * lethal_value:
            dosagebox_text = textinfo(str(dose) + ':Eeffective but overdose beginning at hour ' + \
                                      str(overdose_hour), 215, dosagebox_text_y, 12, win, 'orange')
            deathinfo_text = textinfo(
                'With a dose of ' + str(dose) + ' mg every 8 hours the patient began feeling discomfort at hour' \
                + str(overdose_hour), 400, 50, 15, win, 'black')

        if drug_in_blood_c >= 250 + 2.5 * lethal_value:
            dosagebox_text = textinfo(str(dose) + ':Lethal', 215, dosagebox_text_y, 12, win, 'red')
            deathinfo_text = textinfo('With a dose of ' + str(dose) + ' mg every 8 hours the patient died at hour ' \
                                      + str(lethal_hour), 400, 50, 15, win, 'black')

        dosagebox_text_y -= 35
        clickpoint = False
        x2, y2 = click(win)
        if 900 <= x2 <= 1150 and 10 <= y2 <= 50:
            clickpoint = True
        while not clickpoint:
            x2, y2 = click(win)
            if 900 <= x2 <= 1150 and 10 <= y2 <= 50:
                clickpoint = True

    instruction_text3 = textinfo('Click to END the program', 775, 150, 20, win, 'blue')
    win.getMouse()
    win.close()


main()
