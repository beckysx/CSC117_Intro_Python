# XU SONG
# 24th Oct
# string lab


def validDNA(DNAstring):
    valid = True
    for letter in DNAstring:
        if letter not in 'TACG':
            valid = False
    return valid


def difference(DNA1, DNA2):
    different = 0
    for index in range(len(DNA1)):
        if DNA1[index] != DNA2[index]:
            different += 1
    return different


def complement(DNA):
    complement = ''
    for letter in DNA:
        if letter == 'A':
            complement += 'T'
        if letter == 'T':
            complement += 'A'
        if letter == 'C':
            complement += 'G'
        if letter == 'G':
            complement += 'C'
    return complement


def getTriplets(DNA):
    list_triplet = []
    index = 0
    length = len(DNA)
    partitions = length // 3
    for num in range(1, partitions + 1):
        start = (num - 1) * 3
        end = num * 3
        triplet = DNA[start:end]
        list_triplet.append(triplet)
    return list_triplet


def getAcid(triplet):
    file = open('standardcode.txt', 'r')
    code = file.readline()
    testcode = []
    while code != "":
        code = code.rstrip('\n')
        testcode.append(code)
        code = file.readline()
    file.close()
    for record in testcode:
        if triplet == record[0:3]:
            letter = record[4]
    return letter


def getAminoAcids(list_triplet):
    final = ''
    for triplet in list_triplet:
        letter = getAcid(triplet)
        final += letter
    return final


def main():
    # read from mouse
    mousefile = open('mouse.txt', 'r')
    mouseDNA = mousefile.read()
    mousefile.close()

    # read from possum
    possumfile = open('possum.txt', 'r')
    possumDNA = possumfile.read()
    possumfile.close()

    mouseTest = validDNA(mouseDNA)
    possumTest = validDNA(possumDNA)
    test = True
    if mouseTest and possumTest:
        print('Both strands are valid.')
    else:
        test = False
        if not possumTest:
            print(possumDNA, 'is not valid.')
        if not mouseTest:
            print(mouseDNA, 'is not valid.')

    if test:
        different = difference(mouseDNA, possumDNA)
        print('Strand differ in', different, 'places')
        print(mouseDNA, ' mouse')
        mouse_co = complement(mouseDNA)
        possum_co = complement(possumDNA)
        print(mouse_co, ' mouse-complement')
        print(possumDNA, ' possum')
        print(possum_co, ' possum-comlement')

        list_triplet_mouse = getTriplets(mouseDNA)
        list_triplet_possum = getTriplets(possumDNA)
        m_letter = getAminoAcids(list_triplet_mouse)
        p_letter = getAminoAcids(list_triplet_possum)
        print(m_letter, ' mouse')
        print(p_letter, ' possum')


    else:
        print('try another DNA strand')


main()
