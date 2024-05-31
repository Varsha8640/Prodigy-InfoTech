def is_valid(board, row, col, num):
  """Checks if placing `num` at `(row, col)` is valid."""

  # Check row
  for x in range(9):
    if board[row][x] == num:
      return False

  # Check column
  for x in range(9):
    if board[x][col] == num:
      return False

  # Check 3x3 box
  start_row = row - row % 3
  start_col = col - col % 3
  for i in range(3):
    for j in range(3):
      if board[i + start_row][j + start_col] == num:
        return False

  return True


def solve_sudoku(board):
  """Solves a Sudoku board using backtracking."""

  for row in range(9):
    for col in range(9):
      if board[row][col] == 0:
        for num in range(1, 10):
          if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
              return True

            # Backtrack if the current number leads to a dead end
            board[row][col] = 0

        return False  # No valid number found for this cell

  return True  # All cells are filled correctly


# Example Sudoku board (0 represents empty cells)
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
  print("Sudoku Solved!")
  for row in board:
    print(row)
else:
  print("No solution exists.")