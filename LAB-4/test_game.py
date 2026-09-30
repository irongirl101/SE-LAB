import unittest

from board import Board
from game import DotsAndBoxes
from rules import parse_move, valid_move


class BoardTests(unittest.TestCase):
    def test_valid_horizontal_move(self):
        board = Board()
        self.assertTrue(valid_move(board, "H", 0, 0))
        board.add_line("H", 0, 0)
        self.assertFalse(valid_move(board, "H", 0, 0))

    def test_valid_vertical_move(self):
        board = Board()
        self.assertTrue(valid_move(board, "V", 0, 0))
        board.add_line("V", 0, 0)
        self.assertFalse(valid_move(board, "V", 0, 0))

    def test_invalid_or_repeated_move(self):
        board = Board()
        with self.assertRaises(ValueError):
            board.add_line("H", -1, 0)
        board.add_line("H", 0, 0)
        with self.assertRaises(ValueError):
            board.add_line("H", 0, 0)

    def test_box_completion_assigns_owner(self):
        board = Board()
        for move in (("H", 0, 0), ("V", 0, 0), ("H", 1, 0)):
            board.add_line(*move, player=1)
        completed = board.add_line("V", 0, 1, player=2)
        self.assertEqual(completed, {(0, 0)})
        self.assertEqual(board.owners[(0, 0)], 2)

    def test_end_of_game_condition(self):
        board = Board(rows=1, cols=1)
        for move in (("H", 0, 0), ("H", 1, 0), ("V", 0, 0), ("V", 0, 1)):
            board.add_line(*move)
        self.assertTrue(board.is_complete())


class GameTests(unittest.TestCase):
    def test_scoring_move_keeps_turn_and_updates_score(self):
        game = DotsAndBoxes(rows=1, cols=1)
        for move in (("H", 0, 0), ("V", 0, 0), ("H", 1, 0)):
            game.make_move(*move)
        game.current = 1
        game.make_move("V", 0, 1)
        self.assertEqual(game.scores, [0, 1])
        self.assertEqual(game.current, 1)

    def test_move_after_completion_is_rejected(self):
        game = DotsAndBoxes(rows=1, cols=1)
        for move in (("H", 0, 0), ("H", 1, 0), ("V", 0, 0), ("V", 0, 1)):
            game.board.add_line(*move)
        with self.assertRaises(ValueError):
            game.make_move("H", 0, 0)

    def test_parse_move_rejects_malformed_input(self):
        self.assertEqual(parse_move("h 1 2"), ("H", 1, 2))
        self.assertIsNone(parse_move("H one 2"))
        self.assertIsNone(parse_move("V 1 2 extra"))


if __name__ == "__main__":
    unittest.main()