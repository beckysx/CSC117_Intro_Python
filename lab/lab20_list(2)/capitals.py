# Xu Song
# 19th Oct

def readCapitals(filename):
    file = open(filename, 'r')
    outer_list = []
    statename = file.readline()
    while statename != "":
        statename = statename.rstrip('\n')
        capital = file.readline()
        capital = capital.rstrip('\n')
        latitude = file.readline()
        longitude = file.readline()
        latitude = latitude.rstrip('\n')
        longitude = longitude.rstrip('\n')
        separate = file.readline()
        latitude = float(latitude)
        longitude = float(longitude)
        inner_list = [statename, capital, latitude, longitude]
        outer_list.append(inner_list)
        statename = file.readline()
    file.close()
    return outer_list


def printCapitals(outer_list):
    for record in outer_list:
        for item in record:
            print('{0:<15}'.format(item), end='')
        print()


def Southern(listName):
    southernList = []
    for record in listName:
        if record[2] < 39.72222:
            southernList.append(record)
    return southernList


def findLongitude(capitalname, listName):
    for record in listName:
        if record[1] == capitalname:
            return record[-1]


def westOf(longtitude, listName):
    westernList = []
    for record in listName:
        if record[-1] < longtitude:
            westernList.append(record)
    return westernList


def main():
    us_list = readCapitals('us-state-capitals.txt')
    print(us_list)

    printCapitals(us_list)

    southernStates = Southern(us_list)
    printCapitals(southernStates)

    capitalname = input('Enter a capital: ')
    longtitude = findLongitude(capitalname, us_list)
    westernList = westOf(longtitude, us_list)
    printCapitals(westernList)


main()
