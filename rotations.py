def rotate_row_col(v, turn):
    row, col = v
    match turn:
        case "left":
            return (-col, row)
        case "right":
            return (col, -row)
        case "back":
            return (-row, -col)
        case _:
            raise ValueError(f"Invalid turn input to rotate_row_col: {turn}")
