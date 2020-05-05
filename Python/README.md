## Python Version

The SudokuCreator.py file is used to create a sudoku, and the sudokuSolver.py will provide all possible solutions for that Sudoku.


There is a possibility that the sudoku created by our program will have more than 1 solutions. This is because in the sudokuGenerator() function, we are randomly inserting numbers 1-9 in a board in accordance to the general sudoku standards and then randomly replacing 2/4 of the elements with 0.
We aren't creating a sudoku with the intention of it having just 1 possible solution, even though that's the way usually sudoku's are created.

###### PS, 0 represents null spaces in the sudoku

The solving() function in sudokuSolver.py will give all possible solutions. We have used the principle of backtracking to solve the sudoku.

# Thanks for reading this :)
