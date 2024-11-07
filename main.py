# Programmers:  Paige Ronan
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 11/07/2024
# Programming Assignment:  PA03
# Problem Statement:  program that draws circles lines and designs based off of user input
# Data In: what design, circle: what character the circle is made out of, lines: how many lines, what the lines were
# made out of, how many characters in each line
# Data Out:  the drawing of cirlces, lines, and designs
# Credits:  inspiration for cat:https://www.pinterest.com/pin/327848047858770007/
# inspiration for giraffe:https://www.pinterest.com/pin/315674255104127538/
# inspiration for fish:https://www.wikihow.com/Create-a-Fish-Using-Keyboard-Symbols

import random

#Purpose: draw circle
#Parameters: None
#Return: None
def circle():
    symbol = input('What symbol do you want to make the circle?\n'
                   'You can pick slashes(/), underscore(_), and/or dashes(-)')
    while symbol != '/' and symbol != '_' and symbol != '-':
        print('That is not a valid symbol')
        symbol = input('What symbol do you want to make the circle?\n'
                       'You can pick slashes(/), underscore(_), and/or dashes(-)')
    while symbol == '/' or symbol == '_' or symbol == '-' or not symbol == 'quit':
        print(f'\t\t{symbol}\n'
              f'    {symbol}\t\t {symbol}\n'
              f'  {symbol}\t\t\t   {symbol}\n'
              f'    {symbol}\t\t {symbol}\n'
              f'\t\t{symbol}')
        symbol = input('What symbol do you want to make the circle?\n'
                       'You can pick slashes(/), underscore(_), and/or dashes(-)\n'
                       'Type quit to stop')

#Purpose: draw lines
#Parameters: None
#Return: None
def lines_draw():
    lines = input('How many lines do you want?')
    symbol = input('What symbol do you want to make the lines?')
    characters = input('How many characters do you want on each line?')
    while not characters.isdigit():
        print('That is not a valid input, please enter a number')
        characters = input('How many characters do you want on each line?')
    while not lines.isdigit():
        print('That is not a valid input, please enter a number')
        lines = input('How many lines do you want on each line?')
    count = 0
    while not count >= int(lines):
        print(f'{symbol * int(characters)}')
        count += 1

#Purpose: draw designs at random
#Parameters: None
#Return: None
def random_design():
    one = 0
    two = 0
    three = 0
    design = random.randint(1,3)
    if design == 1:
        print(f'  ><(((°>\n'
              f'><(((°>\n'
              f'  ><(((°>')
    elif design == 2:
        print(f'  /)ii/) \n'
              f' (o " ) \n'
              f'   |  |  \n'
              f'   | o|  \n'
              f'   |  |_______||  \n'
              f'   |      o    | \n'
              f'   |  o______ o| \n'
              f'   || ||    || || \n'
              f'   || ||    || ||')
    elif design == 3:
        print(f'    /|___/| \n'
              f'   (  ^.^  )\n'
              f'    (") (")__/)')

#Purpose: ask user what they want
#Parameters: None
#Return: None
def main():
    print('This program draws different designs based on user input')
    choice = input('What design do you want?\n'
                   'Circle(c)\n'
                   'Set of lines(l)\n'
                   'Random design(r)')
    while choice != 'e':
        if choice == 'c':
            circle()
        elif choice == 'l':
            lines_draw()
        elif choice == 'r':
            random_design()
        choice = input('What design do you want?\n'
                       'Circle(c)\n'
                       'Set of lines(l)\n'
                       'Random design(r)\n'
                       'Exit(e)')
main()
