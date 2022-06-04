# from tic
# from tic_tac_toe_winner import tic_tac_toe_winner
from tic_tac_toe_winner import InvalidMatrix, tic_tac_toe_winner
import pytest

# @pytest.mark.skip(reason="Not possible to test at this time")
def test_matrix_not_3x3_raises_error():
    # arrange
    matrix = [['X', 'O', 'X'], ['O','X','O']]
    # act
    
    # assert
    with pytest.raises(InvalidMatrix):
        tic_tac_toe_winner(matrix)

# @pytest.mark.skip(reason="Not possible to test at this time")
def test_not_all_valid_chars_in_matrix_raises_error():
    matrix = [['O', 'P', 'X']]
    
    with pytest.raises(InvalidMatrix):
        tic_tac_toe_winner(matrix)
    
# @pytest.mark.skip(reason="Not possible to test at this time")
def test_invalid_rel_num_Xs_Os_raises_error():
    matrix_more_O = [
        ['O', 'O', 'O'],
        ['X', 'X', 'X'],
        ['O', 'O', '']
    ]
    matrix_more_X = [
        ['O', 'O', 'O'],
        ['X', 'X', 'X'],
        ['X', 'X', '']
    ]
    # assert
    with pytest.raises(InvalidMatrix):
        tic_tac_toe_winner(matrix_more_O)

    with pytest.raises(InvalidMatrix):
        tic_tac_toe_winner(matrix_more_X)

@pytest.mark.skip(reason="Not possible to test at this time")
def test_x_winner_board_not_full():
    # arrange
    matrix = [
            ['X', 'O', 'O'],
            ['O', 'X', 'O'],
            ['', '', 'X']
            ]
    # act
    result = tic_tac_toe_winner(matrix)
    # assert
    assert result == 'X'
    
        



@pytest.mark.skip(reason="Not possible to test at this time")
def test_nominal_board():
    # nominal test case
    # Arrange
    board = [['X', 'X', 'X'],
            ['O', 'O', ''],
            ['', '', 'O']]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'X'

@pytest.mark.skip(reason="Not possible to test at this time")
def test_empty_board():
    # edge test case
    board = [['', '', ''],
            ['', '', ''],
            ['', '', '']]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result is None

@pytest.mark.skip(reason="Not possible to test at this time")
def test_tied():
    # alternative test case
    # Arrange
    board = [['O', 'X', 'X'],
            ['X', 'O', 'O'],
            ['X', 'O', 'X']]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'Tie'
