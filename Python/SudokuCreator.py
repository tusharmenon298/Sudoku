import numpy as np;
from random import sample;

innerSide=3;
outerSide=innerSide*innerSide

def patternGenerator(r,c): return ( innerSide * (r % innerSide) + r // innerSide + c) % outerSide

def shuffler(s): return sample(s,len(s))

def sudokuGenerator():
    #We create a board which has all the numbers
    base = range(innerSide)
    rows  = [ g*innerSide + r for g in shuffler(base) for r in shuffler(base) ]
    cols  = [ g*innerSide + c for g in shuffler(base) for c in shuffler(base) ]
    nums  = shuffler(range(1,innerSide*innerSide+1))

    board = [ [nums[patternGenerator(r,c)] for c in cols] for r in rows ]

    #Now we remove the numbers to create our sudoku

    totalElements = outerSide*outerSide
    emptyElements = totalElements * 2//4
    for p in sample(range(totalElements),emptyElements):
        board[p//outerSide][p%outerSide] = 0

    return board


