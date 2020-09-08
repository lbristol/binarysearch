import random
import time

class main:
    def __init__(self,input):
        self.input = input
        self.list = []

    def randomgen(self):
        i = random.randint(1,9)
        self.list = range(i, 1000000, 3)

    def find(self):
        start = time.time()
        if len(self.list) == 1:
            if self.input == self.list[0]:
                end = time.time()
                return print(str(self.input) + " has been found in " + str((end-start)/1000) + " seconds! Good guess.")
            else:
                end = time.time()
                return print(str(self.input) + " has not been found. The search took " + str((end-start)/1000) + " seconds.")
        elif len(self.list) % 2 == 0:
            h = int(len(self.list) / 2)
        else:
            h = int(len(self.list) // 2)

        if self.input < self.list[h]:
            self.list = self.list[:h]
            self.find()
        else:
            self.list = self.list[h:]
            self.find()


while True:
    x = input("Enter another number? y/n ")
    if x.isalpha():
        if x.upper() == "Y":
            y = input("Enter a non-decimal number here: ")
            if y.isnumeric() and "." not in y:
                go = main(int(y))
                go.randomgen()
                go.find()
            else:
                print("Looks like you made a typo.")
        elif x.upper() == "N":
            break
        else:
            print("Looks like you made a typo.")
    else:
        print("Looks like you made a typo.")
