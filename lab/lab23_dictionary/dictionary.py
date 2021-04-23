# XU SONG
# 26th Oct
# lab 23

def main():
    # step 1
    misspell = {'teh': 'the', 'theif': 'thief', 'dum': 'dumb'}
    for key, value in misspell.items():
        print(key, ':', value)

    # step 2
    file = open('misspellings.txt', 'r')
    line = file.readline()
    line = line.rstrip('\n')
    line = line.replace(':', ' ')
    listofItem = []
    while line != "":
        line = line.split()
        listofItem.append(line)
        line = file.readline()
        line = line.rstrip('\n')
        line = line.replace(':', ' ')
    dictionary = dict(listofItem)
    file.close()
    for key, value in dictionary.items():
        print(key, value)

    # step 3
    checkfile = open('checkme.txt', 'r')
    sentence = checkfile.read()
    print(sentence)
    checkfile.close()

    # step 4
    sentence = sentence.split()
    new_sentence = []
    for word in sentence:
        if word in dictionary:
            word = dictionary[word]
            new_sentence.append(word)
        else:
            new_sentence.append(word)
    new_sentence = ' '.join(new_sentence)
    fixedfile = open('fixed.txt', 'w')
    fixedfile.write(new_sentence)
    fixedfile.close()

    # step 5
    fixedfile = open('fixed.txt', 'r')
    count = {}
    sentence = fixedfile.read()
    sentence = sentence.split()
    for word in sentence:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    fixedfile.close()
    print(count)
    fixedfile = open('fixed.txt', 'a')
    for key, value in count.items():
        value = str(value)
        fixedfile.write(key + ':' + value + '\n')
    fixedfile.close()


main()
