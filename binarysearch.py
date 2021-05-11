import random
import time

class main:
    def __init__(self, input, rangeinput):
        self.input = input
        self.rangeinput = rangeinput
        self.list = []

    def randomgen(self):
        i = random.randint(1, self.rangeinput)
        # print(i)
        self.list = range(0, 100000000, i)
        # for j in range(10):
        #     print(self.list[j])

    def benchmark(self):
        start = time.time()
        if self.input in self.list:
            end = time.time()
            return (end-start)/1000
        else:
            end = time.time()
            return (end-start)/1000


    def find(self):
        start = time.time()
        if len(self.list) == 1:
            if self.input == self.list[0]:
                end = time.time()
                finaltime = (end-start)/1000
                return print(str(self.input) + " has been found. The search took " + str(finaltime) + " seconds. (Binary Search Algorithm; " +
                    str((finaltime/self.benchmark())*100) + "% the speed of Python3 'in' operator (" + str(self.benchmark()) + " seconds))")
            else:
                end = time.time()
                finaltime = (end-start)/1000
                return print(str(self.input) + " has not been found. The search took " + str(finaltime) + " seconds. (Binary Search Algorithm; " +
                    str((finaltime/self.benchmark())*100) + "% the speed of Python3 'in' operator (" + str(self.benchmark()) + " seconds))")
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
        x = input("Play again? y/n ")
        try:
            if x.upper() == "Y":
                try:
                    print("We're going to play a guessing game.")
                    print("You'll help determine some probabilistic parameters,")
                    print("a random number generator will determine how many items will show up in a list of numbers ranging from 1 to 100,000,000,")
                    print("and you'll guess a number. If it's on the list, you win!")
                    print("\n \n")
                    print("The interval between items in the list, or step, determines how many items are in the list.")
                    rangeinput = int(input("Enter a maximum value for the step (interval between items in the list) between 1 and 100 (no decimals): "))
                    if rangeinput < 1:
                        print("The number you entered is too low.")
                    if rangeinput > 100:
                        print("The number you entered is too high.")
                    # print(rangeinput)
                    input = int(input("Enter a positive integer here - this is your guess (remember - no decimals!): "))
                    if input < 1:
                        print("The number you entered is too low.")
                    if input > 100000000:
                        print("The number you entered is too high.")
                    # print(input)
                    go = main(input, rangeinput)
                    go.randomgen()
                    # print("randomgen done")
                    go.find()
                    # print("find done")
                except (ValueError, TypeError) as e:
                    print(e)
            elif x.upper() == "N":
                break
            else:
                print("ELSE Looks like you made a typo.")
        except (ValueError, TypeError) as e:
            print(e)
