#optimizing TTT
cords = [" ", " ", " ", " "," ", " "]

numbers = [0, 1, 2, 3, 4, 5, 6 , 7, 8]

turn = 0

def board1(cord):

    cords[numbers[cord-1]] = "X"
    print(cords)

def board2(cord):

    cords[numbers[cord - 1]] = "X"
    print(cords)

def moves():
    if turn % 2 == 0:

        try:
            move1 = int(input("Number: "))
            board1(move1)
            numbers[move1-1] = "gone"
            print(numbers)
            turn += 1
        except:
            print("Invalid")
            moves()

    if turn % 2 != 0:
        try:
            move2 = int(input("Number: "))
            board2(move2)
            print(numbers)
            turn +=1
        except:
            print("Invalid")
            moves()


moves()