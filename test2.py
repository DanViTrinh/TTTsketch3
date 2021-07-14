

turn = 0

cords = [" ", " ", " ", " "," ", " "," ", " ", " "]

numbers = [0, 1, 2, 3, 4, 5, 6 , 7, 8]

def w_condition():
    a = cords[0]
    b = cords[1]
    c = cords[2]
    d = cords[3]
    e = cords[4]
    f = cords[5]
    g = cords[6]
    h = cords[7]
    i = cords[8]

w_condition()

x1 = [a , b, c]
x2 = [d , e, f]
x3 = [g, h, i]

y1 = [a , d, g]
y2 = [b, e, h]
y3 = [c , f, i]

d1 = [a, e, i]
d2 = [c , e, g]

# if x1 or

def board1(cord):

    cords[numbers[cord-1]] = "X"
    print(cords)

def board2(cord):

    cords[numbers[cord - 1]] = "O"
    print(cords)

while 0 <= turn <= 8:

    if turn % 2 == 0:

        try:
            move1 = int(input("Number: "))
            board1(move1)
            numbers[move1-1] = "gone"
            print(numbers)
            turn += 1
            w_condition()
            print(x1)

        except:
            print("Invalid")


    if turn % 2 != 0:
        try:
            move2 = int(input("Number: "))
            board2(move2)
            numbers[move2 - 1] = "gone"
            print(numbers)
            turn +=1

        except:
            print("Invalid")


else:
    print("game over")
