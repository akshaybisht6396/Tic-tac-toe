import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        # Game state variables
        self.current_player = "X"  # Player X starts
        self.board = [""] * 9  # Empty board

        # Create a Canvas for the game board
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()

        # Draw the grid
        self.draw_grid()

        # Bind mouse clicks
        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_grid(self):
        """Draws the Tic-Tac-Toe grid with black lines."""
        self.canvas.create_line(100, 0, 100, 300, width=4, fill="black")  # Vertical line 1
        self.canvas.create_line(200, 0, 200, 300, width=4, fill="black")  # Vertical line 2
        self.canvas.create_line(0, 100, 300, 100, width=4, fill="black")  # Horizontal line 1
        self.canvas.create_line(0, 200, 300, 200, width=4, fill="black")  # Horizontal line 2

    def handle_click(self, event):
        """Handles a click on the canvas."""
        # Determine the row and column of the click
        row = event.y // 100
        col = event.x // 100
        idx = row * 3 + col

        # If the cell is empty, make a move
        if self.board[idx] == "":
            self.board[idx] = self.current_player
            self.draw_symbol(row, col, self.current_player)
            
            # Check for a winner
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
                return
            
            # Check for a draw
            if all(cell != "" for cell in self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return
            
            # Switch players
            self.current_player = "O" if self.current_player == "X" else "X"

    def draw_symbol(self, row, col, player):
        """Draws a player's symbol (X or O) on the board."""
        x1 = col * 100 + 20
        y1 = row * 100 + 20
        x2 = (col + 1) * 100 - 20
        y2 = (row + 1) * 100 - 20

        if player == "X":
            self.canvas.create_line(x1, y1, x2, y2, width=4, fill="blue")
            self.canvas.create_line(x1, y2, x2, y1, width=4, fill="blue")
        else:
            self.canvas.create_oval(x1, y1, x2, y2, width=4, outline="red")

    def check_winner(self):
        """Checks if the current player has won."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        for condition in win_conditions:
            if (self.board[condition[0]] == self.current_player and
                self.board[condition[1]] == self.current_player and
                self.board[condition[2]] == self.current_player):
                return True
        return False

    def reset_game(self):
        """Resets the game for a new round."""
        self.board = [""] * 9
        self.current_player = "X"
        self.canvas.delete("all")
        self.draw_grid()

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
