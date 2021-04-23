# Xu Song
# 5th Oct 2018
# Lab 17


# STEP 3

def copyFile(filename):
    # open new file in writing mode
    newFile = open(filename, 'w')
    # open people file in reading mode
    peopleFile = open('people.txt', 'r')

    for name in peopleFile:
        # read from people.txt
        name = name.rstrip('\n')
        # write into new file
        newFile.write(name + '\n')

    # close file
    newFile.close()
    peopleFile.close()


def main():
    # STEP 1
    # open file, writing mode
    openFile = open('people.txt', 'w')
    # ask for names
    name = input("Type name('Done'to quite): ")
    while name != 'Done':  # sentinel
        # write on txt
        openFile.write(name + '\n')
        # adk for next name
        name = input("Type name('Done'to quite): ")
    # close the file
    openFile.close()

    # STEP 2
    # open file,reading mode
    openFile = open('people.txt', 'r')
    for name in openFile:
        name = name.rstrip('\n')
        # print on console
        print(name)
    # close file
    openFile.close()

    # STEP 3
    copyFile('newfile.txt')


main()
