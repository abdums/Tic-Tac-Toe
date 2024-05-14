from tkinter import *
import random

# Global variables for game setup
players = ["El Humangus", "El Computador"]
player = random.choice(players)
buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
label = None

# Game logic Functions

def next_turn():
    pass

def check_winner():
    pass

def empty_spaces():
    pass

def new_game():
    pass

# Game Bone structure
def main():
    global label
    # Initialising the Tkinter window
    window = Tk()
    window.title("Tic-Tac-Toe")

    # Creating game widgets
    label = Label(text=player + "'s turn", font=('consolas', 40))
    label.pack(side="top")

    reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
    reset_button.pack(side="top")

    frame = Frame(window)
    frame.pack()
    
    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                           command=lambda row=row, column=column: next_turn(row, column))
            buttons[row][column].grid(row=row, column=column)

    # Return label so it can be accessed outside of main()
    return label

if __name__ == '__main__':
    label = main()  # Capture the label returned by main()
    label.mainloop()  # Start the main event loop for the label widget