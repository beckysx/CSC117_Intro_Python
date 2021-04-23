# Xu Song
# lab 08 Loops part1
# 12nd Sep 2018
import time

# Step 1

sleep = 'You are feeling very sleepy.'
for s in range(10):
    print(sleep)

# Step 2

message = input('Enter your message: ')
times = int(input('How many times would you like to display your message? '))
for display in range(times):
    print(message)

# Step 3

# Sequence A

s1 = 1
for add in range(100):
    s1 = s1 + 3
    # strategy 1
    ##    print('number=',add,'output:',s1)
    print(s1)

# Sequence B

s2 = 0
for times in range(100):
    s2 = times * times
    # strategy 2
    print(s2)

# Sequence C

s3 = 1
for double in range(100):
    s3 = s3 * 2
    # strategy 3
    ##    time.sleep(0.5)
    print(s3)

# Sequence D

s4 = 0
for add1 in range(100):
    s4 = s4 + add1
    # test
    ##    print('number=',add1,'output:',s4)
    print(s4)

# Sequence E

num1 = 1
num2 = 1
print(num1)
print(num2)
for rabbit in range(98):
    final = num1 + num2
    num1 = num2
    num2 = final
    # test
    ##    print(num1,num2,final)
    print(final)
