from board import Board
from rules import parse_move

class DotsAndBoxes:
    def __init__(self, rows=2, cols=2):
        self.board = Board(rows, cols)
        self.current = 0
        self.scores = [0, 0]

    def make_move(self, orientation, row, col):
        if self.board.is_complete():
            raise ValueError("The game is already complete.")

        completed = self.board.add_line(orientation, row, col, self.current + 1)
        self.scores[self.current] += len(completed)
        if not completed:
            self.current = 1 - self.current
        return completed

    def run(self):
        print("Dots and Boxes")
        print("Enter moves as H row col or V row col.")
        print("Rows and columns start at 0.")
        print("Example: H 0 1")

        while not self.board.is_complete():
            self.board.display(self.scores, self.current)
            raw = input(f"Player {self.current + 1}, move: ").strip().upper()
            move = parse_move(raw)
            if move is None:
                print("Invalid format. Use H row col or V row col.")
                continue

            orientation, row, col = move
            try:
                completed = self.make_move(orientation, row, col)
            except ValueError:
                print("Invalid or already-used move.")
                continue

            if completed:
                print(f"Player {self.current + 1} completed {len(completed)} box(es) and plays again.")
            else:
                print("No box completed; turn passes to the other player.")

        self.board.display(self.scores, self.current)
        print("Game over!")
        if self.scores[0] == self.scores[1]:
            print("The game is a draw.")
        else:
            winner = 1 if self.scores[0] > self.scores[1] else 2
            print(f"Player {winner} wins!")
