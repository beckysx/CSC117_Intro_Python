# XU SONG
# lab 25
# Customer class
# 5th Nov 2018

##Attributes:
##__last_name(str)
##__first_name(str)
##__email_address(str)
##__money_spent(float)

class Customer:

    def __init__(self, last_name, first_name, email, money_spent):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__email = email
        self.__money_spent = money_spent

    def getFname(self):
        return self.__first_name

    def setFname(self, first_name):
        self.__first_name = first_name

    def getLname(self):
        return self.__last_name

    def setLname(self, last_name):
        self.__last_name = last_name

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getMoneyspent(self):
        return self.__money_spent

    def setMoneyspent(self, money):
        self.__money_spent += money

    def makelist(self):
        return [self.__last_name, self.__first_name, str(self.__email), str(self.__money_spent)]
