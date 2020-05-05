import numpy as np
from SudokuCreator import sudokuGenerator as sg


sudoku=sg()

print("Here is the sudoku\n")
print(np.matrix(sudoku))

#This checks if we can add a number at a position
def positionChecker(r,c,num):
    global sudoku
    #This is for checking if number exists in that row and colum
    for i in range(0,9):
        if sudoku[r][i]==num:
            return False
        if sudoku[i][c]==num:
            return False
    #Now to check if number exists in the inner square
    innerSquareX=(r//3)*3
    innerSquareY=(c//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[innerSquareX+i][innerSquareY+j]==num :
                return False
    return True

def solving():
    global sudoku
    #Finds empty element
    for eleY in range(9):
        for eleX in range(9):
            if sudoku[eleX][eleY]==0:
                for n in range(1,10):
                    if positionChecker(eleX,eleY,n)==True:
                        sudoku[eleX][eleY]=n
                        solving()
                        #Backtracking
                        sudoku[eleX][eleY]=0
                return
    print(np.matrix(sudoku))
    print("\n")
    input("Let's see if more solutions")        
