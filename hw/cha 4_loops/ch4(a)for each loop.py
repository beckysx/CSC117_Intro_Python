# Xu Song
# 12nd Sep 2018
# ch(4) loops1

# 4 Distance traveled


speed = int(input('What is the speed of the vehicle in mph?'))
time = int(input('How many hours has it traveled?'))
print('Hour', 'Distance Traveled', sep='  ')
for output in range(1, time + 1):
    distant = speed * output
    print(output, distant, sep='      ')

# 6 Celsius to Fahrenheit


print('Celcius    Fahrenheit')
for celsius in range(21):
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, fahrenheit, sep='          ')

# 12 Population

number = int(input('Starting number of organisms: '))
increase = float(input('Average daily increase: '))
day = int(input('Number of days to multiply: '))

print('Day Approximate   Population')
for output in range(1, day + 1):
    pop = number * (1.3 ** (output - 1))
    print(output, '%.2f' % pop, sep='                   ')
