from tkinter import *
from tkinter import messagebox
import random
import onevsone

def start_game(option):
    if option == "1v1":
        # Start 1v1 game
        start_1v1_game()
    elif option == "1vComputer":
        # Start 1vComputer game
        start_1vComputer_game()
    elif option == "Instructions":
        # Show instructions
        show_instructions()
    elif option == "Quit":
        # Quit the game
        window.quit()

def start_1v1_game():
    # Initialize players and buttons within the 1v1 game function
    players = ["x", "o"]
    player = random.choice(onevsone.players)
    buttons = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    # Creating game widgets
    label = Label(text=player + " turn", font=('consolas', 40))
    label.pack(side="top")

    reset_button = Button(text="restart", font=('consolas', 20), command=onevsone.new_game)
    reset_button.pack(side="top")

    frame = Frame(onevsone.window)
    frame.pack()

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                           command=lambda row=row, column=column: onevsone.next_turn(row, column))
            buttons[row][column].grid(row=row, column=column)

def start_1vComputer_game():
    # Put 1vComputer game logic here
    pass

def show_instructions():
    # Show instructions in a messagebox
    messagebox.showinfo("Instructions", "To be established")

# Initialize the Tkinter window
window = Tk()
window.title("Tic-Tac-Toe")

# Main menu frame
main_menu_frame = Frame(window)
main_menu_frame.pack()

# Main menu options
menu_options = ["1v1", "1vComputer", "Instructions", "Quit"]

# Create main menu buttons
for option in menu_options:
    button = Button(main_menu_frame, text=option, font=('consolas', 20), width=20,
                    command=lambda o=option: start_game(o))
    button.pack(pady=5)

# Start the main event loop
window.mainloop()
