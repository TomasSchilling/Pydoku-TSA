import random

def is_valid(board, row, col, num):
    """Check if num can be placed at board[row][col] without violating Sudoku rules."""
    # Check the row
    if num in board[row]:
        return False
    
    # Check the column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check the 3x3 square
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def fill_board(board):
    """Fill the Sudoku board with numbers from 1 to 9."""
    def fill_cell(row, col):
        if row == 9:
            return True
        if col == 9:
            return fill_cell(row + 1, 0)
        if board[row][col] != 0:
            return fill_cell(row, col + 1)
        
        nums = list(range(1, 10))
        random.shuffle(nums)
        
        for num in nums:
            if is_valid(board, row, col, num):
                board[row][col] = num
                if fill_cell(row, col + 1):
                    return True
                board[row][col] = 0
        
        return False
    
    fill_cell(0, 0)

def remove_numbers(board, difficulty):
    """Remove numbers from the board based on difficulty."""
    if difficulty == 'easy':
        num_cells_to_remove = random.randint(15, 20)
    elif difficulty == 'medium':
        num_cells_to_remove = random.randint(30, 40)
    elif difficulty == 'hard':
        num_cells_to_remove = random.randint(55, 58)
    elif difficulty == 'hardest':
        num_cells_to_remove = random.randint(61, 62)
    else:
        raise ValueError("Invalid difficulty level. Choose from 'easy', 'medium', or 'hard'.")
    
    cells_removed = 0
    while cells_removed < num_cells_to_remove:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            cells_removed += 1

def generate_sudoku(difficulty):
    """Generate a Sudoku puzzle with the specified difficulty."""
    # Create an empty board
    board = [[0] * 9 for _ in range(9)]
    
    # Fill the board with numbers
    fill_board(board)
    
    # Remove some numbers to create the puzzle
    remove_numbers(board, difficulty)
    
    return board

