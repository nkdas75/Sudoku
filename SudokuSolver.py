# Sudoku Solver
#Simple but brut force method.
#Find an empt position - position filled with '0'
#Fill that position starting with 1 and check if row, colum and 3x3 (box constraints) are met.
#If the constraints are satisfied, move to the next empty slot recurssively till all slots are filled.
# If constraints are not satisfied backtrack
#check https://www.wikiwand.com/en/Sudoku_solving_algorithms#/Backtracking for details


solveThis_old =     [[0, 7, 0, 2, 3, 8, 0, 0, 0],
                 [0, 0, 0, 7, 4, 0, 8, 0, 9],
                 [0, 6, 8, 1, 0, 9, 0, 0, 2],
                 [0, 3, 5, 4, 0, 0, 0, 0, 8],
                 [6, 0, 7, 8, 0, 2, 5, 0, 1],
                 [8, 0, 0, 0, 0, 5, 7, 6, 0],
                 [2, 0, 0, 6, 0, 3, 1, 9, 0],
                 [7, 0, 9, 0, 2, 1, 0, 0, 0],
                 [0, 0, 0, 9, 7, 4, 0, 8, 0]]

solveThis = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]



def findEmptyPosition(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                return True, row, column
    return False, 0, 0


def foundIn3by3Grid(puzzle, number, row, col):
    for i in range(3):
        for j in range(3):
            if number == puzzle[i + row][j + col]:
                return True
    return False


def isNumberInRowAndColumn(puzzle, number, row, col):
    if number != puzzle[row][col]:
        if number not in puzzle[row] and number not in [inner[col] for inner in puzzle]:
            return False
    return True


def getNumber(puzzle, i, j):
    for pNumber in range(1, 10):
        for numRow in range(9):
            if pNumber != puzzle[i][j]:
                if pNumber not in puzzle[i] and pNumber not in [inner[j] for inner in puzzle]:
                    if foundIn3by3Grid(puzzle, pNumber, i, j):
                        solveThis[i][j] = pNumber


def formatSudoku(puzzle):
    for i in range(9):
        for j in range(9):
            print(puzzle[i][j], end=' ')
        print()


def solve(puzzle):
    found, row, col = findEmptyPosition(puzzle)
    if not found:
        print('I am Done !!!')
        return True
    for num in range(1, 10):
        if isNumberInRowAndColumn(puzzle, num, row, col) == False:
            if foundIn3by3Grid(puzzle, num, (row - row % 3), (col - col % 3)) == False:
                puzzle[row][col] = num
                if solve(puzzle):
                    return True
                puzzle[row][col] = 0
    return False


formatSudoku(solveThis)
solve(solveThis)
formatSudoku(solveThis)
