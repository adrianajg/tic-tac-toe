import pytest

class InvalidMatrix(Exception):
    pass

class GameNotOver(Exception):
    pass

def tic_tac_toe_winner(matrix):
    # Check for valid input
    is_valid = is_valid_input(matrix)
    if not is_valid:
        raise InvalidMatrix
    
    # Check for horizontal win
    for row in matrix:
        if row[0] == row[1] == row[2] and row[0] != '':
            return row[0]
    
    # Check for vertical win
    for i in range(len(matrix[0])):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] and matrix[0][i] != '':
            return matrix[0][i]
    
    # Check for diagonal win
    if matrix[0][0] == matrix[1][1] == matrix[2][2] or matrix[0][2] == matrix[1][1] == matrix[2][0]:
        if matrix[1][1] != '':
            return matrix[1][1]
    
    # Check if more than two blank spaces in matrix
    if is_valid[1] > 0:
        return None
    
    # Return tie
    return "Tie"
    

def is_valid_input(matrix):
    # Check all elements are 'X', 'O', or ''
    num_X = 0
    num_O = 0
    num_space = 0
    for row in matrix:
        for column in row:
            if column not in ['X','O','']:
                return False
            elif column == 'X':
                num_X += 1
            elif column == 'O':
                num_O += 1
            else:
                num_space += 1
            
    # Check number of 'X' between number of 'O' +/- 1
    if num_X < num_O - 1 or num_X > num_O + 1 or num_O < num_X - 1 or num_O > num_X + 1:
        return False
    
    # Check matrix is 3 x 3
    if len(matrix) != 3:
        return False
    if len(matrix[0]) != 3 or len(matrix[1]) != 3 or len(matrix[2]) != 3:
        return False
    
    # Return True and num blank spaces if valid
    return (True, num_space)