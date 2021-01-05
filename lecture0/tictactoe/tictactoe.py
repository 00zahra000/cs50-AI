"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_turn, o_turn = 0, 0
    for row in board:
        for cell in row:
            if cell == X:
                x_turn += 1
            elif cell == O:
                o_turn += 1
    # who played less times, it's their turn now.
    if not terminal(board) and x_turn > o_turn:
        return O
    elif not terminal(board) and x_turn == o_turn:
        return X
    else:
        return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if terminal(board):
        raise ValueError("GAME OVER")
    elif action not in actions(board):
        raise ValueError("Invalid Action.")
    else:
        p = player(board)
        current_board = copy.deepcopy(board)
        (i, j) = action
        current_board[i][j] = p

    return current_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][0] == board[0][1] == board[0][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][0] == board[2][0] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][1] == board[2][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[1][0] == board[1][1] == board[1][2] != None:
        if board[1][0] == X:
            return X
        else:
            return O
    elif board[2][0] == board[2][1] == board[2][2] != None:
        if board[2][0] == X:
            return X
        else:
            return O
    elif board[0][1] == board[1][1] == board[2][1] != None:
        if board[0][1] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][2] == board[2][2] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    elif board[2][0] == board[1][1] == board[0][2] != None:
        if board[2][0] == X:
            return X
        else:
            return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Someone won
    if winner(board) != None:
        return True

    # All cells were filled
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)

    # If empty board is provided as input, return corner.
    if board == initial_state():
        return (0, 0)

    if p == X:
        value = -math.inf
        selected_action = None
        for action in actions(board):
            min = min_value(result(board, action))
            if min > value:
                value = min
                selected_action = action
    elif p == O:
        value = math.inf
        selected_action = None
        for action in actions(board):
            max = max_value(result(board, action))
            if max < value:
                value = max
                selected_action = action

    return selected_action
