# from tic
# from tic_tac_toe_winner import tic_tac_toe_winner
from tic_tac_toe_winner import InvalidMatrix, GameNotOver, tic_tac_toe_winner
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

# @pytest.mark.skip(reason="Not possible to test at this time")
def test_horizontal_win():
    # arrange
    matrix_row_1_win = [
        ['X', 'X', 'X'],
        ['O', 'O', ''],
        ['O', 'X', 'O']
        ]
    matrix_row_2_win = [
        ['X', 'O', 'X'],
        ['O', 'O', 'O'],
        ['X', '', 'X']
    ]
    matrix_row_3_win = [
        ['O','X','X'],
        ['X','','X'],
        ['O','O','O']
    ]
    # act
    row_1_win = tic_tac_toe_winner(matrix_row_1_win)
    row_2_win = tic_tac_toe_winner(matrix_row_2_win)
    row_3_win = tic_tac_toe_winner(matrix_row_3_win)

    # assert
    assert row_1_win == 'X'
    assert row_2_win == 'O'
    assert row_3_win == 'O'

# @pytest.mark.skip(reason="Not possible to test at this time")
def test_vertical_win():
    # arrange
    matrix_column_0_win = [
        ['X', 'O', 'X'],
        ['X', 'O', ''],
        ['X', '', 'O']
        ]
    matrix_column_1_win = [
        ['X', 'O', 'X'],
        ['O', 'O', ''],
        ['X', 'O', 'X']
    ]
    matrix_column_2_win = [
        ['O','','X'],
        ['X','','X'],
        ['O','O','X']
    ]
    # act
    column_0_win = tic_tac_toe_winner(matrix_column_0_win)
    column_1_win = tic_tac_toe_winner(matrix_column_1_win)
    column_2_win = tic_tac_toe_winner(matrix_column_2_win)

    # assert
    assert column_0_win == 'X'
    assert column_1_win == 'O'
    assert column_2_win == 'X'

# @pytest.mark.skip(reason="Not possible to test at this time")
def test_diagonal_win():
    # arrange

@pytest.mark.skip(reason="Not possible to test at this time")
def test_game_not_over():
    # arrange
    pass

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
