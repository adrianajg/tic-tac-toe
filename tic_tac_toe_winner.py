import pytest

class InvalidMatrix(Exception):
    pass

def tic_tac_toe_winner(matrix):
    # Check for valid input
    if not is_valid_input(matrix):
        raise InvalidMatrix
    # Check for game still in progress
    # Check for horizontal win
        # For row in matrix:
            # if all 'X' or all 'O' return row[0]
    # Check for vertical win
        # For column in matrix (i in range len(matrix[0]))
            # if all 'X' or all 'O' return matrix[0][column]
    # Check for diagonal win
        # if matrix[0][0] == [matrix][1][1] == [matrix][2][2] or matrix[0][2] == matrix[1][1] == matrix[2][0] 
            # return matrix[1][1]
    # Check if more than two blank spaces in matrix
        # initialize num_blank_spaces variable
        # for row in matrix
            # for column in row
                # if column == '' incriment num_blank_spaces
        # if num_blank_spaces > 1:
            # return None
    # Return tie
    pass

def is_valid_input(matrix):
    # Check all elements are 'X', 'O', or ''
    num_X = 0
    num_O = 0
    for row in matrix:
        for column in matrix:
            if column not in ['X','O','']:
                return False
            elif column == 'X':
                num_X += 1
            else:
                num_O += 1
            
    # Check number of 'X' between number of 'O' +/- 1
    if num_X < num_O - 1 or num_X > num_O + 1 or num_O < num_X - 1 or num_O > num_X + 1:
        return False
    # Check matrix is 3 x 3
    # Return True if valid, raise InvalidMatrix error otherwise
    return False

def is_game_over(matrix):
    
    pass