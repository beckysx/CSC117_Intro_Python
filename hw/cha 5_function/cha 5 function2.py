# Xu Song
# cha5b
# 29th Sep 2018

# Page 230


# 6


def calory(fat, carb):
    f_calory = fat * 9
    c_calory = carb * 4
    return f_calory, c_calory



# 10

def feet_to_inches(feet):
    inches = 12 * feet
    return inches



# 13

def falling_distance(t):
    g = 9.8
    distance = 1 / 2 * g * (t ** 2)
    return distance





if __name__ == '__main__':
    # 6
    fat = int(input('Enter the number of fat grams you consumed in a day: '))
    carb = int(input('Enter the number of carbohydrate grams you consumed in a day: '))
    f_calory, c_calory = calory(fat, carb)
    print(f'There are {f_calory} calories from {fat} fat grams.\n'
          f'There are {c_calory} calories from {carb} carb grams.')
    # 10
    feet = float(input('Enter a number of feet: '))
    inches = feet_to_inches(feet)
    print(f'There are {inches} inches in {feet} feet.')
    # 13
    for t in range(1, 11):
        distance = falling_distance(t)
        print(t, 's', '%.2f' % distance, 'm')
