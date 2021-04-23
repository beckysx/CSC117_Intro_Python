# Xu Song
# 26th Sep 2018
# Lab 13 Function 1

# factorials
def factorials(n):
    factor = 1
    result = 1
    while factor < n:
        factor = factor + 1
        result = result * factor
    return result


# prime number
def prime(n):
    if n < 2:
        r = False
    else:
        test = 2
        final = n % test
        if final == 0 and n > test:
            r = False
        while test < n and final != 0:
            test += 1
            final = n % test
            if final == 0 and n != test:
                r = False
        if final == 0 and n == test:
            r = True
    return r


def main():
    print('Hello, world')
    for f_repeat in range(21):
        n = f_repeat
        print(n, factorials(n), sep=' ')
    n = 1
    time = 1
    count = 0
    while time <= 1000:
        if prime(n) == True:
            time += 1
            count += 1
            if count % 10 != 0:
                print('{:10d}'.format(n), end='')
            else:
                print('{:10d}'.format(n))
        n += 1

    print('Goodbye, world')


main()
