"""
Tic Tac Toe with AI (Minimax Algorithm)
Description:
    - Human player (X) vs Computer AI (O)
    - AI always plays optimally using Minimax algorithm
    - Demonstrates recursion, backtracking, and decision-making in AI
"""


# Tic-Tac-Toe Board
import math

# Initialize the Tic Tac Toe board (3x3 represented as list of 9 cells)
board = [" " for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == player for i in cond) for cond in win_conditions)

def is_full(board):
    return " " not in board

def minimax(board, depth, is_maximizing):
    if is_winner(board, "O"):  # AI wins
        return 1
    elif is_winner(board, "X"):  # Human wins
        return -1
    elif is_full(board):  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# ------------------ MAIN GAME LOOP ------------------

print("Tic-Tac-Toe: You are X, AI is O")
print_board()

while True:
    # Human move (with input validation)
    try:
        move = int(input("Enter your move (0-8): "))
        if move < 0 or move > 8:
            print("Invalid input! Enter a number between 0 and 8.")
            continue
        if board[move] != " ":
            print("Cell already occupied! Try again.")
            continue
    except ValueError:
        print("Invalid input! Please enter a number between 0 and 8.")
        continue

    board[move] = "X"

    # Check if human wins
    if is_winner(board, "X"):
        print_board()
        print("🎉 You win!")
        break
    if is_full(board):
        print_board()
        print("It's a draw!")
        break

    # AI move
    ai_move = best_move()
    board[ai_move] = "O"

    print_board()

    # Check if AI wins
    if is_winner(board, "O"):
        print("🤖 AI wins!")
        break
    if is_full(board):
        print("🤝 It's a draw!")
        break
