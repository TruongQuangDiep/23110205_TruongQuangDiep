N = 3

row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]

def is_goal_state(board):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == goal

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print("--------")
