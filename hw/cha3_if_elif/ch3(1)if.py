# Xu Song
# 5 Sep 2018
# Homework Ch 3a page 115


# 1 Day of the week
number = int(input('Enter an integer between 1 to 7: '))
if number == 1:
    print('Monday')
if number == 2:
    print('Tuesday')
if number == 3:
    print('Wednesday')
if number == 4:
    print('Thursday')
if number == 5:
    print('Friday')
if number == 6:
    print('Saturday')
if number == 7:
    print('Sunday')
if number > 7:
    print('Error!')

# 2 Areas of Rectangles

w1 = float(input('Enter the width of the first rectangle: '))
l1 = float(input('Enter the length of the first rectangle: '))
w2 = float(input('Enter the width of the first rectangle: '))
l2 = float(input('Enter the width of the first rectangle: '))
a1 = w1 * l1
a2 = w2 * l2
if a1 > a2:
    print('Rectangle 1 has greater area')
if a1 < a2:
    print('Rectangle 2 has greater area')
if a1 == a2:
    print('Two rectangles have same area')

# 3 Age Classifier
age = int(input('Please enter your age: '))
if age <= 1:
    print('he or she is an infant')
if 1 < age < 13:
    print('he or she is a child')
if 13 <= age < 20:
    print('he or she is a teenager')
if age >= 20:
    print('he or she is an adult')
