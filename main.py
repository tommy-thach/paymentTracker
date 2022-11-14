from datetime import date
import os
import pickle
import socket

date = date.today().strftime("%m/%d/%y")
entryList = []

if os.path.isfile('data.dat'):
    with open('data.dat', 'rb') as f:
        entryList = pickle.load(f)
else:
    with open('data.dat', 'wb') as f:
        pickle.dump(dict, f)

if os.path.isfile('settings.ini'):
    if os.stat('settings.ini').st_size != 0:
        with open('settings.ini', 'r') as f:
            user1 = f.readline()
            user2 = f.readline()
else:
    user1 = input("Enter your name: ")
    user2 = input("Enter the name of who your entry is with: ")
    with open('settings.ini', 'w') as f:
        f.write(user1+"\n")
        f.write(user2+"\n")


def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def updateList(eList):
    totalCost = 0
    for i, item in enumerate(eList, 1):
        costList = item.split("$", 1)[1]
        totalCost += float(costList)
        print('{}. {}'.format(i, item))

    with open('data.dat', 'wb') as f:
        pickle.dump(eList, f)

    return totalCost


def addEntry(entryName, entryCost):
    entryList.append('{:<30s}'.format(entryName + " (" + str(date) + ")") + "Cost: $" + format(float(entryCost), '.2f'))
    mainMenu()


def removeEntry(removeIndex):
    entryList.pop(int(removeIndex) - 1)
    mainMenu()


def mainMenu():
    os.system('cls')

    print("Welcome, \033[1;31m" + user1)
    print("\033[0;0mToday is:\033[1;31m", date)
    print("\033[0;0mYour entries are with: \033[1;31m" + user2)
    print("\n\033[0;0mEntries:\033[0;0m")

    totalCost = updateList(entryList)
    print("\nTotal Cost: $" + str(format(float(totalCost), '.2f')))

    print("\n\033[1;31m[Options]\033[0;0m")
    print("1. Add\n2. Remove\n3. Exit\n\033[0;0m")
    usrInput = input("Enter your choice: ")

    while not usrInput.isdigit():
        print('Invalid input.')
        mainMenu()

    if int(usrInput) == 1:
        entryName = input('Enter a name for this entry: ')
        entryCost = input('Enter the cost for this entry: $')

        while not isFloat(entryCost):
            print('\nInvalid input.')
            entryCost = input('Enter the cost for this entry: $')

        addEntry(entryName, entryCost)

    elif int(usrInput) == 2:
        removeIndex = input("""Enter the number you would like to remove (Type "ALL" to remove all): """)

        while not removeIndex.isdigit() and not removeIndex == "ALL":
            print('\nInvalid input.')
            removeIndex = input("""Enter the number you would like to remove (Type "ALL" to remove all): """)

        if removeIndex == "ALL":
            entryList.clear()
            mainMenu()
        else:
            removeEntry(removeIndex)

    elif int(usrInput) == 3:
        print('Exiting..')

    else:
        print('Invalid input.')
        mainMenu()


mainMenu()
