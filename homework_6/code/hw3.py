from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    flatten_board = [element for row in board for element in row]
    all_lines = [
        flatten_board[:3], flatten_board[3:6], flatten_board[6:],
        flatten_board[::3], flatten_board[1::3], flatten_board[2::3],
        flatten_board[::4], flatten_board[2:8:2],
    ]
    for line in all_lines:
        set_line = set(line)
        if len(set_line) == 1 and "-" not in set_line:
            return f"{set_line.pop()} wins!"
    if "-" not in flatten_board:
        return "draw!"
    return "unfinished!"


if __name__ == '__main__':
    board = [['-', '-', 'o'], 
             ['-', 'o', 'o'], 
             ['x', 'x', 'x']]
    print(tic_tac_toe_checker(board))