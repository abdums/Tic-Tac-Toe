from tkinter import *
from tkinter import messagebox
import random

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
    # Put 1v1 game logic here
    pass

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
