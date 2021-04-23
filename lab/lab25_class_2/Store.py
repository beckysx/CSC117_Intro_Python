# XU SONG
# Lab 25
# 5th Nov 2018
# main function


from Item import *
from Customer import *


def main():
    program = True

    selection = int(input('1-List Inventory \n2-Add Item \n3-Search Inventory\
                          \n4-Delete Item\n5-Create Customer \n6-Delete Customer\
                          \n7-Update Customer \n8-Exit \nEnter Number: '))

    if selection == 8:
        program = False

    while program:

        if selection == 1:
            inventoryfile = open('inventory.txt', 'r')
            line = inventoryfile.readline()
            while line != '':
                line = line.rstrip('\n')
                line = line.split(',')
                for a in line:
                    print('{0:<10}'.format(a), end='')
                print()
                line = inventoryfile.readline()
            inventoryfile.close()

        if selection == 2:
            inventoryfile = open('inventory.txt', 'a')
            name = input('Name: ')
            price = float(input('Price: '))
            item_type = input('Item type: ')
            quantity = int(input('Quantity: '))
            name = Item(name, price, item_type, quantity)
            inventoryfile.write(','.join(name.makelist()) + '\n')
            inventoryfile.close()

        if selection == 3:
            name = input('Enter name: ')
            inventoryfile = open('inventory.txt', 'r')
            line = inventoryfile.readline()
            itemlist = []
            while line != '':
                line = line.rstrip('\n')
                line = line.split(',')
                obj = Item(line[0], line[1], line[2], line[3])
                itemlist.append(obj)
                line = inventoryfile.readline()

            namelist = []
            for obj in itemlist:
                namelist.append(obj.getName())
                if name == obj.getName():
                    print(obj.getQ())

            if name not in namelist:
                print('No such item')

            inventoryfile.close()

        if selection == 4:

            name = input('Enter Name: ')

            inventoryfile = open('inventory.txt', 'r')
            line = inventoryfile.readline()
            itemlist = []
            while line != '':
                line = line.rstrip('\n')
                line = line.split(',')
                obj = Item(line[0], line[1], line[2], line[3])
                itemlist.append(obj)
                line = inventoryfile.readline()

            index = 0
            for obj in itemlist:
                if name == obj.getName():
                    del itemlist[index]
                index += 1
            inventoryfile.close()

            inventoryfile = open('inventory.txt', 'w')
            for obj in itemlist:
                inventoryfile.write(','.join(obj.makelist()) + '\n')
            inventoryfile.close()

            print()
            print('Item is deleted!')

        if selection == 5:
            customerfile = open('customer.txt', 'a')
            lname = input('Last Name: ')
            fname = input('First Name: ')
            email = input('E-mail Adress: ')
            money = float(input('Money spent: '))
            lname = Customer(lname, fname, email, money)
            customerfile.write(','.join(lname.makelist()) + '\n')
            customerfile.close()

        if selection == 6:

            lname = input('Enter Last Name: ')
            fname = input('Enter First Name: ')

            customerfile = open('customer.txt', 'r')
            line = customerfile.readline()
            customerlist = []
            while line != '':
                line = line.rstrip('\n')
                line = line.split(',')
                obj = Customer(line[0], line[1], line[2], line[3])
                customerlist.append(obj)
                line = customerfile.readline()

            index = 0
            cusnamelist = []
            for obj in customerlist:
                cusnamelist.append(obj.getLname() + obj.getFname())
                if lname == obj.getLname() and fname == obj.getFname():
                    del customerlist[index]
                    print()
                    print('The customer is deleted!')
                    print()
                index += 1

            if lname + fname not in cusnamelist:
                print()
                print("Can't find the customer!")
                print()

            customerfile.close()

            customerfile = open('customer.txt', 'w')
            for obj in customerlist:
                customerfile.write(','.join(obj.makelist()) + '\n')
            customerfile.close()

        if selection == 7:

            lname = input('Enter Last Name: ')
            fname = input('Enter First Name: ')
            moneyIncrease = float(input('Enter money spent: '))

            customerfile = open('customer.txt', 'r')
            line = customerfile.readline()
            customerlist = []
            while line != '':
                line = line.rstrip('\n')
                line = line.split(',')
                obj = Customer(line[0], line[1], line[2], line[3])
                customerlist.append(obj)
                line = customerfile.readline()
            customerfile.close()

            for obj in customerlist:
                if lname == obj.getLname() and fname == obj.getFname():
                    nobj = obj.makelist()
                    del nobj[-1]
                    nobj.append(obj.setMoneyspent(moneyIncrease))
                    obj = Customer(nobj[0], nobj[1], nobj[2], nobj[3])

            customerfile = open('customer.txt', 'w')
            for obj in customerlist:
                customerfile.write(','.join(obj.makelist()) + '\n')

            customerfile.close()

        selection = int(input('Enter Number: '))

        if selection == 8:
            program = False


main()
