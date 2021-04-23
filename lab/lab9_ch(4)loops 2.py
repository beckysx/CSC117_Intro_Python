# Xu Song
# Loop2
# 14th Sep 2018

import random

# Step 1

score = int(input('Enter score(type a negative score to stop):'))
total = 0
times = 0
while score >= 0:
    total = total + score
    score = int(input('Enter score(type a negative score to stop):'))
    times = times + 1
if times == 0:
    print('Error')
else:
    average = total / times
    print('Average of the', times, 'scores is', average)

# Step 2

temp = float(input('Enter a temperature: '))
while temp < 94.0 or temp > 107.0:
    print('Out of range')
    temp = float(input('Re-enter a temperature: '))
print('You entered', temp, 'degrees.')

# Step 3

print('I am thinking of a number between 1 and 1024 inclusive./nSee if you can guess what it is!')
computer = random.randint(1, 1024)
guess = int(input('Enter your guess: '))
while guess != computer:
    if guess > computer:
        print('No,your guess is too high.')
    else:
        print('No,your guess is too low.')
    guess = int(input('Enter your guess: '))
print('Yes, that is exactly right! The number is', computer)
