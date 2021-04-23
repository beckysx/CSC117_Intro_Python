# Lab07 Rock Paper Scissors Lizard Spock
# Xu Song
# 10th Sep 2018


import random

version = int(input(
    'Which version do you want to choose? \nType 1 for human VS computer \nType 2 for computer VS computer \nYour choice: '))

# rules
# rock=1
# paper=2
# scissors=3
# lizard=4
# spock=5

# human vs computer version
if version == 1:
    hum = int(input('rock=1\npaper=2\nscissors=3\nlizard=4\nspock=5\nMake your choice(1 to 5):'))
    com = random.randint(1, 5)
    print(com)

    # hum win
    if hum == 1 and (com == 3 or com == 4):
        print('You win!')
        if com == 3:
            print('Because Rock crushes Scissors')
        if com == 4:
            print('Because Rock crushes Lizard')
    elif hum == 2 and (com == 1 or com == 5):
        print('You win!')
        if com == 1:
            print('Because Paper covers Rock')
        if com == 5:
            print('Because Paper disproves Spock')
    elif hum == 3 and (com == 2 or com == 4):
        print('You win!')
        if com == 2:
            print('Because Scissors cuts Paper')
        if com == 4:
            print('Because Scissors decapitates Lizard')
    elif hum == 4 and (com == 5 or com == 2):
        print('You win!')
        if com == 5:
            print('Because Lizard poisons Spock')
        if com == 2:
            print('Because Lizard eats Paper')
    elif hum == 5 and (com == 3 or com == 1):
        print('You win!')
        if com == 3:
            print('Because Spock smashes Scissors')
        if com == 1:
            print('Because Spock vaporizes Rock')

    # com win
    elif com == 1 and (hum == 3 or hum == 4):
        print('Computer wins!')
        if hum == 3:
            print('Because Rock crushes Scissors')
        if hum == 4:
            print('Because Rock crushes Lizard')
    elif com == 2 and (hum == 1 or hum == 5):
        print('Computer wins!')
        if hum == 1:
            print('Because Paper covers Rock')
        if hum == 5:
            print('Because Paper disproves Spock')
    elif com == 3 and (hum == 2 or hum == 4):
        print('Computer wins!')
        if hum == 2:
            print('Because Scissors cuts Paper')
        if hum == 4:
            print('Because Scissors decapitates Lizard')
    elif com == 4 and (hum == 5 or hum == 2):
        print('Computer wins!')
        if hum == 5:
            print('Because Lizard poisons Spock')
        if hum == 2:
            print('Because Lizard eats Paper')
    elif com == 5 and (hum == 3 or hum == 1):
        print('Computer wins!')
        if hum == 3:
            print('Because Spock smashes Scissors')
        if hum == 1:
            print('Because Spock vaporizes Rock')

    # tie
    elif com == hum:
        print('Tie! No winner')


# computer vs computer version

else:

    print('rock=1\npaper=2\nscissors=3\nlizard=4\nspock=5')
    c1 = random.randint(1, 5)
    c2 = random.randint(1, 5)
    print('Player 1:', c1, '\nPlayer 2:', c2)

    # Player1 wins
    if c1 == 1 and (c2 == 3 or c2 == 4):
        print('Player1 wins')
        if c2 == 3:
            print('Because Rock crushes Scissors')
        if c2 == 4:
            print('Because Rock crushes Lizard')
    elif c1 == 2 and (c2 == 1 or c2 == 5):
        print('Player1 wins')
        if c2 == 1:
            print('Because Paper covers Rock')
        if c2 == 5:
            print('Because Paper disproves Spock')
    elif c1 == 3 and (c2 == 2 or c2 == 4):
        print('Player1 wins')
        if c2 == 2:
            print('Because Scissors cuts Paper')
        if c2 == 4:
            print('Because Scissors decapitates Lizard')
    elif c1 == 4 and (c2 == 5 or c2 == 2):
        print('Player1 wins')
        if c2 == 5:
            print('Because Lizard poisons Spock')
        if c2 == 2:
            print('Because Lizard eats Paper')
    elif c1 == 5 and (c2 == 3 or c2 == 1):
        print('Player1 wins')
        if c2 == 3:
            print('Because Spock smashes Scissors')
        if c2 == 1:
            print('Because Spock vaporizes Rock')

    # Player2 wins
    elif c2 == 1 and (c1 == 3 or c1 == 4):
        print('Player2 wins')
        if c1 == 3:
            print('Because Rock crushes Scissors')
        if c1 == 4:
            print('Because Rock crushes Lizard')
    elif c2 == 2 and (c1 == 1 or c1 == 5):
        print('Player2 wins')
        if c1 == 1:
            print('Because Paper covers Rock')
        if c1 == 5:
            print('Because Paper disproves Spock')
    elif c2 == 3 and (c1 == 2 or c1 == 4):
        print('Player2 wins')
        if c1 == 2:
            print('Because Scissors cuts Paper')
        if c1 == 4:
            print('Because Scissors decapitates Lizard')
    elif c2 == 4 and (c1 == 5 or c1 == 2):
        print('Player2 wins')
        if c1 == 5:
            print('Because Lizard poisons Spock')
        if c1 == 2:
            print('Because Lizard eats Paper')
    elif c2 == 5 and (c1 == 3 or c1 == 1):
        print('Player2 wins')
        if c1 == 3:
            print('Because Spock smashes Scissors')
        if c1 == 1:
            print('Because Spock vaporizes Rock')

    # tie
    elif c1 == c2:
        print('Tie! No winner')
