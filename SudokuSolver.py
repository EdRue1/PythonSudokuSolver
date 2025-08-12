from array import *

class SudokuSolver:
    GRID_SIZE = 9

    @staticmethod
    def main():
        board = [[0, 9, 7, 0, 8, 0, 4, 0, 0],
                [0, 4, 0, 0, 0, 5, 7, 8, 0],
                [0, 6, 0, 0, 0, 7, 0, 1, 0],
                [9, 0, 6, 0, 7, 0, 0, 4, 3],
                [4, 0, 3, 2, 0, 6, 0, 0, 8],
                [8, 0, 1, 3, 0, 9, 0, 0, 0],
                [6, 8, 5, 1, 3, 0, 0, 0, 0],
                [0, 3, 4, 5, 9, 0, 2, 6, 0],
                [0, 1, 0, 0, 6, 0, 0, 0, 0]]

        SudokuSolver.printBoard(board, SudokuSolver.GRID_SIZE)

        #fill check to see if solved here
        if (SudokuSolver.solveBoard(board, SudokuSolver.GRID_SIZE)):
            print("Solved Successfully")
        else:
            print("Unsolvable Board")

        SudokuSolver.printBoard(board, SudokuSolver.GRID_SIZE)

    @staticmethod
    def printBoard(board, GRID_SIZE):
        for row in range(GRID_SIZE):
            if (row % 3 == 0 and row != 0):
                print("---------------------")
            for column in range(GRID_SIZE):
                if (column % 3 == 0 and column != 0):
                    print("|", end=" ")
                print(board[row][column], end=" ")
            print()

    @staticmethod
    def isNumberInRow(board, number, row, GRID_SIZE):
        for i in range(GRID_SIZE):
            if board[row][i] == number:
                return True
        return False
    
    @staticmethod
    def isNumberInColumn(board, number, column, GRID_SIZE):
        for i in range(GRID_SIZE):
            if board[i][column] == number:
                return True
        return False
        
    @staticmethod
    def isNumberInBox(board, number, row, column):
        localBoxRow = row - row % 3
        localBoxColumn = column - column % 3
        i = localBoxRow
        j = localBoxColumn

        for i in range(localBoxRow, localBoxRow + 3):
            for j in range(localBoxColumn, localBoxColumn + 3):
                if board[i][j] == number:
                    return True
        return False
    
    @staticmethod
    def isValidPlacement(board, number, row, column, GRID_SIZE):
        return (not SudokuSolver.isNumberInRow(board, number, row, GRID_SIZE)) and \
        (not SudokuSolver.isNumberInColumn(board, number, column, GRID_SIZE)) and \
        (not SudokuSolver.isNumberInBox(board, number, row, column))

    @staticmethod
    def solveBoard(board, GRID_SIZE):
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                if board[row][column] == 0:
                    for numberToTry in range(1, GRID_SIZE + 1):
                        if (SudokuSolver.isValidPlacement(board, numberToTry, row, column, GRID_SIZE)):
                            board[row][column] = numberToTry

                            if(SudokuSolver.solveBoard(board, GRID_SIZE)):
                                return True
                            else:
                                board[row][column] = 0
                    return False
        return True

if __name__ == '__main__':
    SudokuSolver.main()