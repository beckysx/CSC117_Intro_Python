# Xu Song
# Lab 10 loops3
# 19th Sep 2018


# Step 1 Find the biggest value

value = 1
num = float(input('Enter value ' + str(value) + ' : '))
big = num
while num > 0:
    value += 1
    num = float(input('Enter value ' + str(value) + ' : '))
    if num > big:
        big = num
print('The largest value is:', big)

# Step 2 Find the Hour

time = 1
temp = float(input('What was the temp at ' + str(time) + ' AM? '))
low = temp
position = 1
for track in range(8):
    time += 1
    temp = float(input('What was the temp at ' + str(time) + ' AM? '))
    if temp < low:
        low = temp
        position = time
print('The lowest temperature first occurred at', position, 'AM.')

# Step 3 Find the sum of positive numbers

factor = int(input('Enter an integer (0 to quit): '))
product = 1
if factor > 0:
    product *= factor
while factor != 0:
    factor = int(input('Enter an integer (0 to quit): '))
    if factor > 0:
        product *= factor
print('The product of the positive numbers is', product)

# Step 4 Decide whether a Number is prime


na = int(input('Enter a natural number: '))
if na < 2:
    print('NOT PRIME')
else:
    test = 2
    final = na % test
    if final == 0 and na > test:
        print('NOT PRIME')
    while test < na and final != 0:
        test += 1
        final = na % test
        if final == 0 and na != test:
            print('NOT PRIME')
    if final == 0 and na == test:
        print('PRIME')
