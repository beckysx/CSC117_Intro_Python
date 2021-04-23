# Xu Song
# 20th Oct
# Page 336 homework

def winTime(filename, item):
    fileopen = open(filename, 'r')
    line = fileopen.readline()
    line = line.rstrip('\n')
    count = 0
    while line != "":
        if line == item:
            count += 1
            line = fileopen.readline()
            line = line.rstrip('\n')
        else:
            line = fileopen.readline()
            line = line.rstrip('\n')
    fileopen.close()
    return count


def testLoShu(listName):
    test = False
    r1 = listName[0][0] + listName[0][1] + listName[0][2]
    r2 = listName[1][0] + listName[1][1] + listName[1][2]
    r3 = listName[2][0] + listName[2][1] + listName[2][2]
    c1 = listName[0][0] + listName[1][0] + listName[2][0]
    c2 = listName[0][1] + listName[1][1] + listName[2][1]
    c3 = listName[0][2] + listName[1][2] + listName[2][2]
    x1 = listName[0][0] + listName[1][1] + listName[2][2]
    x2 = listName[0][2] + listName[1][1] + listName[2][0]
    if r1 == r2 == r3 == c1 == c2 == c3 == x1 == x2:
        test = True
    return test


def main():
    teamname = input('Enter the team name: ')
    win = winTime('WorldSeriesWinners.txt', teamname)
    print(teamname, 'won', win, 'times.')

    Loshu = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    if testLoShu(Loshu):
        print('It is a Lo Shu Magic Square.')


main()
