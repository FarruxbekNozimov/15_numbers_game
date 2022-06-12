from os import system
import random as r

"""
Plan:
1. Printing the preliminary board
2. Enter the values from User
    W --> Up
    S --> Down
    A --> Left
    D --> Right
3. Checking the board
4. Moving the numbers
5. Showing Winner
6. Play again?
"""

numbers = [['1 ', '2 ', '3 ', '4 '], ['5 ', '6 ', '7 ', '8 '], ['9 ', '10', '11', '12'], ['13', '14', '  ', '15']]
answers = numbers.copy()
r.shuffle(numbers)


def show_board():
    system('cls')
    print("\n Up(w) Down(s) Left(a) Right(d)")
    print("_" * 25, end="")
    print()
    for i in range(4):
        print("|     |     |     |     |")
        print(f"|  {numbers[i][0]} |  {numbers[i][1]} |  {numbers[i][2]} |  {numbers[i][3]} |")
        print("|_____|_____|_____|_____|")


def play():
    while True:
        show_board()
        choices = {'w': up, 's': down, 'a': left, 'd': right}
        while True:
            choice = input("\nEnter : ").lower()
            if choice in choices:
                choices[choice]()
                break
            print("Invalid choice")
        if answers == numbers:
            break
    print("You won!")


def up():
    a = 0
    for i in range(4):
        for j in range(4):
            if numbers[i][j] == '  ' and numbers[3][j] != '  ':
                numbers[i][j] = numbers[i + 1][j]
                numbers[i + 1][j] = '  '
                a = 1
        if a == 1:
            break


def down():
    a = 0
    for i in range(4):
        for j in range(4):
            if numbers[i][j] == '  ' and numbers[0][j] != '  ':
                numbers[i][j] = numbers[i - 1][j]
                numbers[i - 1][j] = '  '
                a = 1
        if a == 1:
            break


def left():
    a = 0
    for i in range(4):
        for j in range(4):
            if numbers[i][j] == '  ' and numbers[i][3] != '  ':
                numbers[i][j] = numbers[i][j + 1]
                numbers[i][j + 1] = '  '
                a = 1
            if a == 1:
                break


def right():
    a = 0
    for i in range(4):
        for j in range(4):
            if numbers[i][j] == '  ' and numbers[i][0] != '  ':
                numbers[i][j] = numbers[i][j - 1]
                numbers[i][j - 1] = '  '
                a = 1
            if a == 1:
                break


play()
