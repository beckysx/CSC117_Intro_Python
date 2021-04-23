# XU SONG
# hw cha 8
# 25th Oct 2018
# Page 367


def getNumber(telephone):
    number = ''
    for letter in telephone:
        if letter in '1234567890-':
            number = number + letter
        elif letter in 'ABC':
            number = number + '2'
        elif letter in 'DEF':
            number = number + '3'
        elif letter in 'GHI':
            number = number + '4'
        elif letter in 'JKL':
            number = number + '5'
        elif letter in 'MNO':
            number = number + '6'
        elif letter in 'PQRS':
            number = number + '7'
        elif letter in 'TUV':
            number = number + '8'
        elif letter in 'WXYZ':
            number = number + '9'
    return number


def pigLatin(sentence):
    sentence = sentence.split()
    for index in range(len(sentence)):
        sentence[index] = sentence[index] + sentence[index][0]
        sentence[index] = sentence[index][1:]
        sentence[index] = sentence[index] + 'AY'
    a = ''
    for word in sentence:
        a = a + word + ' '
    return a


def main():
    # problem 5
    telephone = input('Enter the Number: ')
    number = getNumber(telephone)
    print(number)

    # problem 12
    sentence = input('Enter the sentence: ')
    print(pigLatin(sentence))


main()
