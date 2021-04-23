# Xu Song
# CSC 117b Lab03 Conversions
# 31 Aug 2018

dollar = int(input('Enter the number of dollars to conver to Euros:'))
euros = float(dollar * 0.81)
print('$', dollar, 'is worth', euros, 'Euros')

pounds = float(input('Enter the number of pounds:'))
kg = float(pounds * 0.354)
print(pounds, 'pounds is equivalent to', kg, 'kg')

kilo = float(input('Enter the number of kilograms:'))
p = float(kilo / 0.354)
print(kilo, 'kg is equivalent to', p, 'pounds')

divident = int(input('Enter an integer to divide (the divident):'))
divisor = int(input('Enter an integer to divide the first number by (divisor):'))
r1 = float(divident / divisor)
r2 = (divident // divisor)
remainder = (divident % divisor)
print(divident, 'divided by', divisor, '=', r1)
print(divident, 'divided by', divisor, 'using long division =', r2, 'with a remainder of', remainder)
