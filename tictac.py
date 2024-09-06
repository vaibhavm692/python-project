import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("800x600")  # Set the window size to 800x600
        self.player_turn = "X"
        self.move_count = 0  # Initialize move count to 0

        # Create a frame to hold the game board
        self.frame = tk.Frame(self.window, bg="#222222")  # Set frame background to dark gray
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the frame in the window

        # Create the game board
        self.board = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.frame, command=lambda row=i, column=j: self.click(row, column), height=3, width=6, 
                            bg="#333333", fg="#FFFFFF", font=("Arial", 24), relief=tk.RAISED, bd=5)
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.board.append(row)

        # Create the score labels
        self.score_label = tk.Label(self.frame, text="Score: X - 0, O - 0", bg="#222222", fg="#FFFFFF", font=("Arial", 18))
        self.score_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        # Create the reset button
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, bg="#333333", fg="#FFFFFF", 
                                    font=("Arial", 18),relief=tk.RAISED, bd=5)
        self.reset_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def click(self, row, column):
        if self.board[row][column]['text'] == "":
            self.board[row][column]['text'] = self.player_turn
            self.board[row][column]['bg'] = "#444444"  # Change button background to darker gray
            self.move_count += 1  # Increment move count
            if self.check_win():
                messagebox.showinfo("Game Over", f"Player {self.player_turn} wins!")
                self.update_score()
                self.reset()
            elif self.move_count == 9:  # Check if all boxes are filled
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset()
            self.player_turn = "O" if self.player_turn == "X" else "X"

    def check_win(self):
        for row in self.board:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                return True
        for column in range(3):
            if self.board[0][column]['text'] == self.board[1][column]['text'] == self.board[2][column]['text'] != "":
                return True
        if self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] != "":
            return True
        if self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] != "":
            return True
        return False

    def update_score(self):
        score = self.score_label['text'].split(":")[1].split(",")
        if self.player_turn == "X":
            score[0] = str(int(score[0].split("-")[1]) + 1)
        else:
            score[1] = str(int(score[1].split("-")[1]) + 1)
        self.score_label['text'] = "Score: X - " + score[0] + ", O - " + score[1]

    def reset(self):
        self.player_turn = "X"
        self.move_count = 0  # Reset move count
        for row in self.board:
            for button in row:
                button['text'] = ""
                button['bg'] = "#333333"  # Reset button background to light gray

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()