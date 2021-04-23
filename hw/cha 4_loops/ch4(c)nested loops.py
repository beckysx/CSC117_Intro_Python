# Xu Song
# 20th Sep 2018Wha


# Bug Collector


day = 1
bug = int(input('Enter the number of bugs collected on day ' + str(day) + ' : '))
total = bug
for collector in range(4):
    day += 1
    bug = int(input('Enter the number of bugs collected on day ' + str(day) + ' : '))
    total = total + bug
print('The bug collector collected', total, 'bugs in 5 days.')

# 3 Budget Analysis


budget = float(input('Enter your budget for a month: '))
expense = float(input('Enter your expense (enter a negative number to stop): '))
total = expense
while expense >= 0:
    expense = float(input('Enter your expense (enter a negative number to stop): '))
    if expense > 0:
        total = total + expense
        rest = budget - total
if rest > 0:
    print('You spent $', total, '. You are under budget.', sep='')
elif rest == 0:
    print('You spent $', total, '. There is no rest.', sep='')
elif rest < 0:
    print('You spent $', total, '. You are over budget.', sep='')

# 7 Pennies for pay


work = int(input('Enter the number of days you working: '))
day = 1
dollar = 0.01
total = dollar
print('Day1 earned: $0.01')
for working in range(work - 1):
    day += 1
    dollar *= 2
    total += dollar
    print('Day', day, ' earned: $', dollar, sep='')
print('Total pay during', work, 'day is $', '%.2f' % total)

# 13


for r in range(7, 0, -1):
    for c in range(r):
        print('*', end='')
    print('')

# 14


for r in range(6):
    print('#', end='')
    for c in range(r):
        print(' ', end='')
    print('#')
