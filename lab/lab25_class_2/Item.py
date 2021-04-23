# XU SONG
# lab 25
# Item class
# 5th Nov 2018


##Attributes:
##__name(str)
##__price(float)
##__item_type(str)
##__quantity(int)


class Item:

    def __init__(self, name, price, item_type, quantity):
        self.__name = name
        self.__price = price
        self.__item_type = item_type
        self.__quantity = quantity

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def getItem_type(self):
        return self.__item_type

    def setItem_type(self, item_type):
        self.__item_type = item_type

    def getQ(self):
        return self.__quantity

    def setQ(self, quantity):
        self.__quantity = quantity

    def makelist(self):
        return [self.__name, str(self.__price), self.__item_type, str(self.__quantity)]
