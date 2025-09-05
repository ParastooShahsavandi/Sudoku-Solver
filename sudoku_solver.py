import random
import math

# Helper function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

# Helper function to calculate the cost of the board
def calculate_cost(board):
    cost = 0
    for row in board:
        cost += 9 - len(set(row))  # Cost for row duplicates
    for col in range(9):
        col_vals = [board[row][col] for row in range(9)]
        cost += 9 - len(set(col_vals))  # Cost for column duplicates
    return cost

# Initialize the Sudoku board
def initialize_board(puzzle):
    board = [row[:] for row in puzzle]
    for row in board:
        empty_positions = [i for i, val in enumerate(row) if val == 0]
        available_numbers = list(set(range(1, 10)) - set(row))
        random.shuffle(available_numbers)
        for pos in empty_positions:
            row[pos] = available_numbers.pop()
    return board

# Generate a neighbor by swapping two cells in a row
def generate_neighbor(board):
    neighbor = [row[:] for row in board]
    row = random.randint(0, 8)
    cols = [i for i in range(9) if puzzle[row][i] == 0]
    if len(cols) > 1:
        col1, col2 = random.sample(cols, 2)
        neighbor[row][col1], neighbor[row][col2] = neighbor[row][col2], neighbor[row][col1]
    return neighbor

# Simulated Annealing Algorithm
def simulated_annealing(puzzle, max_iterations=50000, initial_temp=100.0, cooling_rate=0.995):
    current_board = initialize_board(puzzle)
    current_cost = calculate_cost(current_board)
    temperature = initial_temp

    for iteration in range(max_iterations):
        if current_cost == 0:
            print(f"Solution found at iteration {iteration}:")
            print_board(current_board)
            return current_board

        neighbor = generate_neighbor(current_board)
        neighbor_cost = calculate_cost(neighbor)
        delta_cost = neighbor_cost - current_cost

        if delta_cost < 0 or random.random() < math.exp(-delta_cost / temperature):
            current_board = neighbor
            current_cost = neighbor_cost

        temperature *= cooling_rate

        if iteration % 1000 == 0 or iteration == max_iterations - 1:
            print(f"Iteration {iteration}: Current Cost = {current_cost}, Temperature = {temperature:.2f}")

    print("No solution found using Simulated Annealing.")
    return None

# Backtracking Solver for fallback
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def sudoku_backtracking_solver(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if sudoku_backtracking_solver(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Example Sudoku puzzle
puzzle = [
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

# Run Simulated Annealing
print("Solving Sudoku using Simulated Annealing:")
solution = simulated_annealing(puzzle)

# Fallback to Backtracking if no solution found
if solution is None:
    print("Switching to Backtracking Solver...")
    if sudoku_backtracking_solver(puzzle):
        print("Solved Sudoku using Backtracking:")
        print_board(puzzle)
    else:
        print("No solution exists.")
