# Xu Song
# 17th Oct

def main():
    # STEP 1
    moviefile = open('movies.txt', 'r')
    line = moviefile.readline()
    myList = []
    while line != "":
        line = line.rstrip('\n')
        myList.append(line)
        line = moviefile.readline()
    moviefile.close()
    myList.append('Top Gun')
    print(myList)

    # STEP 2

    # first method
    num_myList = len(myList)
    print(num_myList)

    # second method
    count = 0
    for item in myList:
        count += 1
    print(count)

    # STEP 3

    # first method
    if 'Adventures in Babysitting' in myList:
        print('Yes')
    else:
        print('No')

    # second method
    for item in myList:
        if item == 'Adventures in Babysitting':
            print('yes')

    # Step 4

    # first method
    half1 = myList[0:5]
    half2 = myList[5:11]
    print(half2 + half1)

    # second method
    count2 = 0
    half3 = []
    for item in myList:
        count2 += 1
        if count2 > 5:
            half3.append(item)

    count2 = 0
    for item in myList:
        count2 += 1
        if count2 <= 5:
            half3.append(item)

    print(half3)

    # STEP 5

    # first method
    print(myList[4])

    # second method
    count3 = 0
    for item in myList:
        count3 += 1
        if count3 == 5:
            print(item)

    # STEP 6

    # first method
    myList.reverse()
    print(myList)

    myList.reverse()

    # second method
    myList_reverse = myList[::-1]
    print(myList_reverse)

    # STEP 7

    myList.sort()
    print(myList)

    # STEP 8

    # first method
    minimum = min(myList)
    maximum = max(myList)
    print('Min:', minimum, '\nMaximum:', maximum)

    # second method
    maxi = 'A'
    mini = 'z'
    for item in myList:
        if item > maxi:
            maxi = item
        if item < mini:
            mini = item
    print('Min:', mini, '\nMaximum:', maxi)

    # STEP 9
    myList.insert(4, 'Spaceballs')
    print(myList)

    # STEP 10
    myList.remove("Ferris Bueller's Day Off")
    print(myList)

    myList.insert(3, "Ferris Bueller's Day Off")

    # STEP 11
    del myList[4]
    print(myList)

    # STEP 12
    print(myList.index('The Goonies'))


main()
