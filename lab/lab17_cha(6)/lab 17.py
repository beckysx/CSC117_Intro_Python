# Xu Song
# lab 17
# 10th Oct 2018


def mistake():
    file = True
    filename = input('Enter the file name:')
    while file:
        try:
            donor = open(filename, 'r')
            return filename
        except FileNotFoundError as err:
            print(err)
            option = input('quit or correct?:')
            if option == 'quit':
                file = False
            if option == 'correct':
                filename = input('Enter the file name:')


def replace():
    swap = open('swap.txt', 'r')
    donor = open('donors.txt', 'w')
    name = swap.readline()
    while name != '':
        name = name.rstrip('\n')
        number = swap.readline()
        number = number.rstrip('\n')
        donor.write(name + '\n')
        donor.write(str(number) + '\n')
        name = swap.readline()
    swap.close()
    donor.close()


def main():
    filename = mistake()
    donor = open(filename, 'r')
    copy = open('swap.txt', 'w')
    name = donor.readline()
    while name != '':
        name = name.rstrip('\n')
        number = donor.readline()
        number = number.rstrip('\n')
        print(name, number)
        delete = input('Delete the person?(type yes or no):')
        if delete == 'yes':
            name = donor.readline()
        if delete == 'no':
            rename = input("Change name('no to use original one'):")
            renumber = int(input("Change number (negative number to use original one):"))
            if rename != 'no' and rename != name:
                copy.write(rename + '\n')
            else:
                copy.write(name + '\n')
            if renumber > 0 and renumber != number:
                copy.write(str(renumber) + '\n')
            else:
                copy.write(str(number) + '\n')

            name = donor.readline()

    donor.close()
    copy.close()

    replace()


main()
