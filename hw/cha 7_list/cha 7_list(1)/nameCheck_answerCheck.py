# Xu Song
# 18th Oct

def girl_boy_names(girl_f_path, boy_f_path):
    girlFile = open(girl_f_path, 'r')
    boyFile = open(boy_f_path, 'r')
    girl_line = girlFile.readline()
    boy_line = boyFile.readline()
    girls = []
    boys = []
    while girl_line != "" or boy_line != "":
        girl_line = girl_line.rstrip('\n')
        boy_line = boy_line.rstrip('\n')
        girls.append(girl_line)
        boys.append(boy_line)
        girl_line = girlFile.readline()
        boy_line = boyFile.readline()
    girlFile.close()
    boyFile.close()
    return girls, boys


def check_answers(student_path, right_path):
    # problem 7
    rightAnswer = ['A', 'C', 'A', 'A', 'D', \
                   'B', 'C', 'A', 'C', 'B', \
                   'A', 'D', 'C', 'A', 'D', \
                   'C', 'B', 'B', 'D', 'A']
    student_file = open(student_path, 'r')
    rightAnswer_file = open(right_path, 'w')
    for i in rightAnswer:
        rightAnswer_file.write(i + '\n')
    rightAnswer_file.close()
    rightAnswer_file = open(right_path, 'r')
    studentAnswer, wrongQuestion = [], []
    correct, wrong, q_index = 0, 0, 0
    lineRight = rightAnswer_file.readline()
    lineStudent = student_file.readline()
    while lineRight != "" and lineStudent != "":
        lineRight = lineRight.rstrip('\n')
        lineStudent = lineStudent.rstrip('\n')
        studentAnswer.append(lineStudent)
        q_index += 1
        if lineRight == lineStudent:
            correct += 1
        else:
            wrong += 1
            wrongQuestion.append(q_index)
        lineRight = rightAnswer_file.readline()
        lineStudent = student_file.readline()
    student_file.close()
    rightAnswer_file.close()
    if correct >= 15:
        print('The student passed the exam.')
    else:
        print('The student failed the exam.')
    print('Total number of correctly answered questions:', correct)
    print('Total number of incorrectly answered questions:', wrong)
    print('These questions are wrong:', wrongQuestion)


def main():
    # Question 7
    check_answers('studentanswer.txt', 'rightanswer.txt')

    # Question 8
    girls, boys = girl_boy_names('GirlNames.txt', 'BoyNames.txt')
    name = input('Enter names:')
    if name in girls:
        print('yes')
    elif name in boys:
        print('yes')
    else:
        print('No such name')


main()
