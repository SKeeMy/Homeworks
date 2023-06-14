import unittest
from code.hw3 import tic_tac_toe_checker


class TestTicTacToe(unittest.TestCase):

    def test_incomplete_board(self):
        board = [['-', '-', 'o'], 
                 ['-', 'o', 'o'], 
                 ['x', 'x', '-']]
        self.assertEqual(tic_tac_toe_checker(board), 'unfinished!')

    def test_draw_board(self):
        board = [['x', 'o', 'x'], 
                 ['x', 'x', 'o'], 
                 ['o', 'x', 'o']]
        self.assertEqual(tic_tac_toe_checker(board), 'draw!')

    def test_x_wins(self):
        board = [['x', 'o', '-'], 
                 ['x', 'x', 'o'], 
                 ['x', 'o', '-']]
        self.assertEqual(tic_tac_toe_checker(board), 'x wins!')

    def test_o_wins(self):
        board = [['o', 'x', '-'], 
                 ['x', 'o', 'x'], 
                 ['-', 'o', 'o']]
        self.assertEqual(tic_tac_toe_checker(board), 'o wins!')

    def test_x_in_the_middle(self):
        board = [['-', '-', '-'], 
                 ['-', 'x', '-'], 
                 ['-', '-', '-']]
        self.assertEqual(tic_tac_toe_checker(board), 'unfinished!')


if __name__ == '__main__':
    unittest.main()