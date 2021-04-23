# XU SONG
# 6th Oct
# Page 289


# 2
def file(filename):
    openFile = open(filename, 'r')
    line = openFile.readline()
    linenumber = 1
    while line != '' and linenumber <= 5:
        line = line.rstrip('\n')
        print(line)
        linenumber += 1
        line = openFile.readline()
    openFile.close()


# 4
def Itemcounter():
    openName = open('people.txt', 'r')
    name = openName.readline()
    count = 0
    while name != '':
        count += 1
        name = openName.readline()
    print(count)
    openName.close()


# 6
def averageNumber():
    openFile = open('number.txt', 'r')
    number = openFile.readline()
    count = 0
    total = 0
    while number != '':
        count += 1
        number = int(number)
        total += number
        number = openFile.readline()
    openFile.close()
    return count, total


def main():
    # 2
    filename = input('Enter the file name: ')
    file(filename)

    # 4
    Itemcounter()

    # 6
    count, total = averageNumber()
    averagenumber = total / count
    print('%.2f' % averagenumber)


main()
