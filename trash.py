
import random
turn = 0
cords = [" ", " ", " ", " "," ", " "," ", " ", " "]
numbers = [0, 1, 2, 3, 4, 5, 6 , 7, 8]

variable1 = 0

while variable1 <= 8:
    "x" + 1 = numbers[]




while 0 <= turn <= 8:
    if turn % 2 == 0:
        try:
            turn += 1
            move1 = int(input("Number: "))
            cords[numbers[move1 - 1]] = "X"
            print(cords)
            numbers[move1-1] = 0.1


        except:
            print("Invalid")
            turn -= 1


    if turn % 2 != 0:
        try:
            turn += 1
            move2 = random.choice(numbers)
            cords[move2] = "O"
            numbers[move2] = 0.01
            print(numbers)
            print(cords)



        except:
            turn -= 1



else:
    print("game over")

