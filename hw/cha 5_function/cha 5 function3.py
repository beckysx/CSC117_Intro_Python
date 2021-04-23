# Xu Song
# hw function 3
# 1st Oct 2018

import random


# STEP 1

# randomly selects two numbers
def rand2(n):
    ran1 = random.randint(1, n)
    ran2 = random.randint(1, n)
    return ran1, ran2


# STEP 2

# return a string A to Z
def int2letter(x):
    letter = chr(x + 64)
    return letter


# STEP 3

# generate pairs of random letters
def randletters():
    ran1, ran2 = rand2(26)
    randomletter1 = int2letter(ran1)
    randomletter2 = int2letter(ran2)
    return randomletter1, randomletter2


# test functions
def main():
    # test rand2(n)
    for i in range(10):
        ran1, ran2 = rand2(6)
        print(ran1, ran2)

    # test int2letter(x)
    for a in range(5):
        x = int(input('Enter a number between 1 and 26:'))
        if 1 <= x <= 26:
            letter = int2letter(x)
            print('Corresponding letter is', letter)
        else:
            print('Corresponding letter is ?')

    # test randletters()
    randomletter1, randomletter2 = randletters()
    while randomletter1 != randomletter2:
        randomletter1, randomletter2 = randletters()
        print(randomletter1, randomletter2)


# call main()
main()
