class Board:
    def __init__(self, rows=2, cols=2):
        if rows < 1 or cols < 1:
            raise ValueError("Board dimensions must be positive.")
        self.rows = rows
        self.cols = cols
        self.horizontal = [[False] * cols for _ in range(rows + 1)]
        self.vertical = [[False] * (cols + 1) for _ in range(rows)]
        self.completed = set()
        self.owners = {}

    def add_line(self, orientation, row, col, player=None):
        if not self.valid_move(orientation, row, col):
            raise ValueError("Invalid or already-used move.")
        if orientation == "H":
            self.horizontal[row][col] = True
        else:
            self.vertical[row][col] = True
        return self._update_completed(player)

    def valid_move(self, orientation, row, col):
        if orientation == "H":
            return 0 <= row <= self.rows and 0 <= col < self.cols and not self.horizontal[row][col]
        if orientation == "V":
            return 0 <= row < self.rows and 0 <= col <= self.cols and not self.vertical[row][col]
        return False

    def _update_completed(self, player=None):
        newly_completed = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if (
                    self.horizontal[r][c]
                    and self.horizontal[r + 1][c]
                    and self.vertical[r][c]
                    and self.vertical[r][c + 1]
                ):
                    box = (r, c)
                    if box not in self.completed:
                        self.completed.add(box)
                        newly_completed.add(box)
                        if player is not None:
                            self.owners[box] = player
        return newly_completed

    def is_complete(self):
        total = self.rows * (self.cols + 1) + self.cols * (self.rows + 1)
        used = sum(map(sum, self.horizontal)) + sum(map(sum, self.vertical))
        return used == total

    def display(self, scores, current):
        print()
        print(f"Scores: P1={scores[0]}  P2={scores[1]} | Turn: P{current + 1}")

        for r in range(self.rows + 1):
            print(".".join("---" if self.horizontal[r][c] else "   " for c in range(self.cols)))
            if r < self.rows:
                middle = []
                for c in range(self.cols + 1):
                    wall = "|" if self.vertical[r][c] else " "
                    middle.append(wall)
                    if c < self.cols:
                        middle.append(" " + str(self.owners.get((r, c), " ")) + " ")
                print("".join(middle))
        print()
