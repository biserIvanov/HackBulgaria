from __future__ import print_function
from time import time
from datetime import datetime
from os.path import expanduser
import glob
import os

orders = {}
files = {}
listFlag = False
takeOrderFlag = False
saveFlag = False
doubleLoad = False


def take(input):
    index = 0
    for i in range(len(input)):
        if input[i] == " ":
            index = i
            break
    customer = input[:index]
    priceString = input[index+1:]
    if not "." in priceString:
        priceString = priceString + ".00"
    if customer in orders:
        orders[customer] = str(float(orders[customer]) + float(priceString))
        if not "." in orders[customer]:
            orders[customer] = orders[customer] + ".00"
        else:
            for i in range(len(orders[customer])):
                if orders[customer][i] == ".":
                    temp = orders[customer][i:]
                    if len(temp) < 3:
                        orders[customer] = orders[customer] + "0"
    else:
        orders[customer] = priceString
    print ("Taking order from " + customer + " for " + priceString)
    takeOrderFlag = True


def status():
    for key in orders:
        print (key + " - " + orders[key])


def save():
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    filename = "orders_" + str(stamp)
    file = open(filename, 'w')
    for key in orders:
        file.write(key + " - " + orders[key] + "\n")  # ?
    file.close()
    print ("done")
    saveFlag = True


def listShow():
    files = {}
    home = expanduser("~")
    os.chdir(home)
    a = 0
    for file in glob.glob("orders_*"):
        files[a+1] = file
        a += 1
    for key in files:
        print ("[" + str(key) + "] - " + files[key])
    listFlag = True


def load(num):
    if not listFlag:    #why listFlag not working propely? (always False)
        print ("Use list command before loading")
    elif takeOrderFlag and not saveFlag:
        if not doubleLoad:
            print ("You have not saved the current order.\
                If you wish to discard it, type load " + num + " again.")
            doubleLoad = True
        else:
            orders = {}
            num = int(num)
            for item in files:
                if item == num:
                    file = open(files[item], "r")
                    content = file.read()
                    print (content)
            doubleLoad = False



def main():
    print ("\nCommands:")
    print ("-take <name> <price>")
    print ("-status")
    print ("-save")
    print ("-list")
    print ("-load <number>")
    print ("-finish")
    command = ""
    while command != "finish":
        if command[:4] == "take":
            take(command[5:])
        elif command == "status":
            status()
        elif command == "save":
            save()
        elif command == "list":
            listShow()
        elif command[:4] == "load":
            load(command[5:])
        command = input("\nEnter command>")


if __name__ == '__main__':
    main()
