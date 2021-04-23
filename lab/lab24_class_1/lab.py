# Xu SONG
# 2nd Nov 2018
# oops

# Problem 2

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def __str__(self):
        return 'Current speed is ' + str(self.__speed)

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed


# Problem 5

class RetailItem:
    def __init__(self, number, description, unit, price):
        self.__number = number
        self.__description = description
        self.__unit = unit
        self.__price = price

    def __str__(self):
        item = '{0:<10}'.format('Item#' + str(self.__number))
        description = '{0:<20}'.format(self.__description)
        unit = '{0:<10}'.format(str(self.__unit))
        price = '{0:<10}'.format(str(self.__price))
        print()

        return item + description + unit + price


def main():
    item1 = RetailItem(1, 'Jacket', 12, 59.95)
    item2 = RetailItem(2, 'Designer Jeans', 40, 34.95)
    item3 = RetailItem(3, 'Shirt', 20, 24.95)
    print(item1, item2, item3, end='')


main()
