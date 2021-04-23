# Xu Song
# 15th Sep 2018
# ch(4) loops2


# 8 Sum of Numbers


number = float(input('Enter a number(negative number to stop): '))
total = 0
while number >= 0:
    total = total + number
    number = float(input('Enter a number(negative number to stop): '))
print('The sum of numbers is', total)

# 9 Ocean Levels


total = 1.6
year = 1
print('Year:', year, 'Height', total, 'mm')
while year < 25:
    year = year + 1
    total = total + 1.6
    print('Year:', year, '  Height:', '%.2f' % total, 'mm', sep='')

# 10 Tuition Increase


tuition = 8000
year = 1
print('Year:', year, '  Tuition:$', tuition, sep='')
while year < 5:
    year = year + 1
    tuition = tuition * 1.03
    print('Year:', year, '  Tuition:$', '%.2f' % tuition, sep='')

# 11


end = int(input('Enter a nonegative integer: '))
factor = 1
result = 1
print(end, '!=1', sep='', end='')
while factor < end:
    factor = factor + 1
    result = result * factor
    print('*', factor, sep='', end='')
print('=', result, sep='')

# 12 Population

number = int(input('Starting number of organisms: '))
increase = float(input('Average daily increase: '))
end = int(input('Number of days to multiply: '))
print('Day Approximate   Population')

day = 1
pop = number
print(day, pop, sep='                  ')
while day < end:
    day = day + 1
    pop = pop * (1 + increase)
    print(day, '%.6f' % pop, sep='                  ')
