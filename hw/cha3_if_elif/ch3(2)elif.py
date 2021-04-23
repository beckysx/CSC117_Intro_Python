# Xu Song
# 7th Sep 2018
# homework ch 3b


# 9.Roulette Wheel Colors

n = int(input('Enter an integer: '))

if n == 0:
    print('The pocket is green')
elif n <= 10 and n % 2 == 1:
    print('The pocket is red')
elif n <= 10 and n % 2 == 0:
    print('The pocket is black')
elif n <= 18 and n % 2 == 1:
    print('The pocket is black')
elif n <= 18 and n % 2 == 0:
    print('The pocket is red')
elif n <= 28 and n % 2 == 1:
    print('The pocket is red')
elif n <= 28 and n % 2 == 0:
    print('The pocket is black')
elif n <= 36 and n % 2 == 1:
    print('The pocket is black')
elif n <= 36 and n % 2 == 0:
    print('The pocket is red')
else:
    print('Error!')

# 13 Shipping Charges

w = float(input('Enter the weight of a package(in pounds)：'))
if w <= 2:
    c = w * 1.5
    print('Shipping cahrges:$', \
          format(c, '.2f'), sep='')
if w <= 6:
    c = w * 3
    print('Shipping cahrges:$', \
          format(c, '.2f'), sep='')
if w <= 10:
    c = w * 4
    print('Shipping cahrges:$', \
          format(c, '.2f'), sep='')
else:
    c = w * 4.75
    print('Shipping cahrges:$', \
          format(c, '.2f'), sep='')

# 15 Time Calculator

s = int(input('Enter a number os seconds: '))
if s < 3600:
    o = s // 60
    print('There are', o, 'minutes in', s, 'seconds.')
if s < 86400:
    o = s // 3600
    print('There are', o, 'hours in', s, 'seconds.')
else:
    o = s // 86400
    print('There are', o, 'days in', s, 'seconds.')
