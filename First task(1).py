import tkinter as tk
import random

class RockPaperScissorsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")

        self.label = tk.Label(master, text="Choose rock, paper, or scissors:")
        self.label.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack()

        self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack()

        self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack()

    def play(self, user_choice):
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return "You win!"
        else:
            return "You lose!"

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGUI(root)
    root.mainloop()
