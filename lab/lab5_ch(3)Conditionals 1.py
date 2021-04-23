# Xu Song
# 2018/9/5
# Lab 05
import random

# Step 1
number = int(input('Enter an integer: '))
if number % 2 == 0:
    print('This number is even')
if number % 2 == 1:
    print('This number is odd')

# Step 2
coin = random.randint(0, 1)
if coin == 0:
    print('Heads')
else:
    print('Tails')

# Step3
guess = int(input('Guess a integer between 1 to 4: '))
choosen = random.randint(1, 4)
if guess > choosen:
    print('Your guess is too high!')
if guess < choosen:
    print('Your guess is too low!')
if guess == choosen:
    print('Your guess is correct!')
print('Thank You for playing')

# Step 4
penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25
half = 0.5
p = int(input('How many pennies do you have?'))
n = int(input('How many nickels do you have?'))
d = int(input('How many dimes do you have?'))
q = int(input('How many quarters do you have?'))
h = int(input('How many half dollars do you have?'))
money = p * penny + n * nickel + d * dime + q * quarter + h * half
if money % 2 == 0:
    print('Your coins added up to a whole number!')
else:
    print('Your coins added up to a whole number plus some additional change!')
