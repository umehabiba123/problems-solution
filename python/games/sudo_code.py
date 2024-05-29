def print_board(board):
    """Helper function to print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty_location(board):
    """Find an empty location on the board (represented by 0)."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def is_valid(board, num, row, col):
    """Check if it's valid to place num in the given row, col."""
    # Check the row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    empty_loc = find_empty_location(board)
    if not empty_loc:
        return True  # No empty locations, puzzle solved
    row, col = empty_loc

    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0  # Undo the move
    
    return False

# main body ....
if __name__ == "__main__":
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    if solve_sudoku(board):
        print("Sudoku puzzle solved successfully:")
        print_board(board)
    else:
        print("No solution exists.")
