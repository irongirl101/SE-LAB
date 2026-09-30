def valid_move(board, orientation, row, col):
    return board.valid_move(orientation, row, col)


def parse_move(raw):
    parts = raw.strip().upper().split()
    if len(parts) != 3:
        return None

    orientation, row, col = parts
    if orientation not in {"H", "V"}:
        return None
    try:
        return orientation, int(row), int(col)
    except ValueError:
        return None


def completed_boxes(board, before):
    return len(board.completed - before)
