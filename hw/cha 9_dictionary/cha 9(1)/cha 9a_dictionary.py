# Xu Song
# 27th Oct 2018

import random


def filetoDic(filename):
    file = open(filename, 'r')
    statename = file.readline()
    statename = statename.rstrip('\n')
    capital = file.readline()
    capital = capital.rstrip('\n')
    seperate = file.readline()
    uslist = []
    statelist = []
    while statename != "":
        statelist.append(statename)
        record = [statename, capital]
        uslist.append(record)
        statename = file.readline()
        statename = statename.rstrip('\n')
        capital = file.readline()
        capital = capital.rstrip('\n')
        seperate = file.readline()
    usdictionary = dict(uslist)
    file.close()
    return statelist, usdictionary


def main():
    # problem 1
    roomnumber = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'NT110': 1244, 'CM241': 1411}
    instructor = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
    time = {'CS101': '8:00 am', 'CS102': '9:00 am', 'CS103': '10:00 am', 'NT110': '11:00 am', 'CM241': '1:00 pm'}
    name = input('Enter the course code: ')
    if name in roomnumber:
        print('Room Number: ', roomnumber[name])
        print('Instructor: ', instructor[name])
        print('Meeting Time: ', time[name])
    else:
        print('Course not Found')

    # problem 2
    statelist, usdictionary = filetoDic('us-state-capitals.txt')
    right = 0
    wrong = 0
    for question in range(5):
        statename = random.choice(statelist)
        answer = input('What is the capital city of ' + statename + '? ')
        if answer == usdictionary[statename]:
            right += 1
        else:
            wrong += 1
            print('Wrong! The capital city of', statename, 'is', usdictionary[statename])
    print('In 10 questions, you got', right, 'right and', wrong, 'wrong.')

    # problem 3
    code = {'A': '~', 'B': '!', 'C': '@', 'D': '#', 'E': '$', 'F': '%', 'G': '^', 'H': '&', 'I': '*', 'J': '(',
            'K': ')', 'L': '_', 'M': '-', 'N': '=', 'O': '+', 'P': '[', 'Q': ']', 'R': '{', 'S': '}', 'T': '|',
            'U': ';', 'V': ':', 'W': ',', 'X': '<', 'Y': '.', 'Z': '>'}
    file = open('file1.txt', 'r')
    sentence = file.read()
    file.close()
    sentence = sentence.upper()
    wordlist = sentence.split()
    codewordlist = []
    for word in wordlist:
        codeword = ''
        for letter in word:
            codeword += code[letter]
        codewordlist.append(codeword)
    print(' '.join(codewordlist))

    file = open('file2.txt', 'r')
    sentence = file.read()
    file.close()
    wordlist = sentence.split()
    keylist = code.keys()
    valuelist = code.values()
    keylist = list(keylist)
    valuelist = list(valuelist)
    newsentence = []
    for word in wordlist:
        english = ''
        for a in word:
            index = valuelist.index(a)
            letter = keylist[index]
            english += letter
        newsentence.append(english)
    newsentence = ' '.join(newsentence)
    print(newsentence)


main()
