"""
Write a module docstring here
"""

__author__ = "Hong Gao"

""" Use this function to format your input/output arguments. Be sure not to change the order of the output arguments. 
    Remember that code organization is very important to us, so we encourage the use of helper fuctions and classes as you see fit.
    
    Input:
        1. input_file (String) = contains the name of a text file you need to read that is in the same directory, includes the ".txt" extension
           (ie. "input.txt")

    Outputs:
        1. final_pos_x (int) = final x location of Pacman
        2. final_pos_y (int) = final y location of Pacman
        3. coins_collected (int) = the number of coins that have been collected by Pacman across all movements
5 5
1 2
NNESEESWNWW
1 0
2 2
2 3
    """

    # return final_pos_x, final_pos_y, coins_collected 

from os import error
from typing import Generic


def pacman(input_file):
    f = open(input_file, 'r')

    line = f.readline()
    matrix = [int(el) for el in line.strip().split(' ')]
    
    line2 = f.readline()
    start=[int(el) for el in line2.strip().split(' ')] 
    
    if start[0] > matrix[0] and start[1] > matrix[1]:
        print((-1,-1,0))
        return
    
    line3 = f.readline()
    moves = line3.strip()
    
    walls = []
    while True:
        line5= f.readline()
        if line5:
            walls.append([int(el) for el in line5.strip().split()])
        else:
            break
    
    f.close()
    
    countercoins=0
    route = []
    route.append(start)
    curr = start
    for move in moves:
    
        if move == "N":
            x = 0
            y = 1
        elif move == "E":
            x = 1
            y = 0
        elif move == "S":
            x = 0
            y = -1
        elif move == "W":
            x = -1
            y = 0
        
        future = [ curr[0]+x, curr[1]+y ]

        if future not in walls and future[0] < matrix[0] and future[0] >= 0 and future[1] < matrix[1] and future[1] >= 0:
            curr = future
            if future not in route:
                route.append(curr)
                countercoins += 1
    print((curr[0], curr[1], countercoins))

pacman('runtime.txt')



