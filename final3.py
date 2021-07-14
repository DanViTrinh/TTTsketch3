import random
turn = 0
cords = [" ", " ", " ", " "," ", " "," ", " ", " "]
numbers = list(range(0, 9))

def w_condition():
    x0 = numbers[0] + numbers[1] + numbers[2]
    x1 = numbers[3] + numbers[4] + numbers[5]
    x2 = numbers[6] + numbers[7] + numbers[8]

    y0 = numbers[0] + numbers[3] + numbers[6]
    y1 = numbers[1] + numbers[4] + numbers[7]
    y2 = numbers[2] + numbers[5] + numbers[8]

    z0 = numbers[0] + numbers[4] + numbers[8]
    z1 = numbers[2] + numbers[4] + numbers[6]

    if x0 or x1 or x2 or y0 or y1 or y2 or z0 or z1 == 0.3:
        print(x1)
        print("You win! ")
        print("Game over")
        end = input("end game? ")
        print(end)

    if x0 or x1 or x2 or y0 or y1 or y2 or z0 or z1 == 0.03:
        print("CPU win! ")
        print("Game over")
        end = input("end game? ")
        print(end)



while 0 <= turn <= 8:
    if turn % 2 == 0:
        try:
            turn += 1
            move1 = int(input("Number: "))
            cords[numbers[move1 - 1]] = "X"
            print(cords)
            numbers[move1-1] = 0.1
            w_condition()

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
            w_condition()


        except:
            turn -= 1



else:
    print("game over")
