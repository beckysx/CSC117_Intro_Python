# Xu Song
# 7th Sep 2018
# Lab 06


# Step 1
money = float(input('Enter the amount of money you spent: '))
if money <= 0.99:
    print('You get 1 point.')
elif money <= 4.99:
    print('You get 3 points.')
elif money <= 9.99:
    print('You get 8 points.')
else:
    print('You get 20 points.')

# Step 2
name = input('Enter the name of the item: ')
cost = float(input('Enter the cost for one item: '))
number = int(input('Enter quantity you want to buy: '))
sub = cost * number
if number <= 5:
    ad = sub
    ms = sub - ad
elif number <= 14:
    ad = sub * 0.95
    ms = sub - ad
elif number <= 26:
    ad = sub * 0.9
    ms = sub - ad
elif number <= 35:
    ad = sub * 0.85
    ms = sub - ad
elif number <= 43:
    ad = sub * 0.8
    ms = sub - ad
else:
    ad = sub * 0.75
    ms = sub - ad
print('Subtotal:$', \
      format(sub, '.2f'), \
      sep='')
print('Total after discount:$', \
      format(ad, '.2f'), \
      sep='')
print('Money saved:$', \
      format(ms, '.2f'), \
      sep='')
'''
Test Cases
Input:item name     price     quantity     subtotal     discount     total
Input:bag           20.05     10           200.5        10.025       190.475
Input:pen           180       43           7740         1548         6192
'''

# Step 3

year = int(input('Enter a year: '))

if year % 4 == 0 and year % 400 == 0:
    print('Year', year, 'is a leap year.')

elif year % 4 != 0:
    print('Year', year, 'is not a leap year. Because it can not divided by 4.')

elif year % 100 != 0:
    print('Year', year, 'is not a leap year. Because it can not divided by 100.')

else:
    print('Year', year,
          'is not a leap year. Because even though it’s divisible by 4, it’s also divisible by 100 but not 400.')
