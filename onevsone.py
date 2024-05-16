from tkinter import *
import random

# Global variables for game setup
players = ["x", "o"]
player = random.choice(players)
buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
label = None

# Game logic functions
def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player
        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))
        elif check_winner() is True:
            label.config(text=(player + " wins!"))
        elif check_winner() == "Tie":
            label.config(text="Tie!")

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="purple")
            buttons[row][1].config(bg="purple")
            buttons[row][2].config(bg="purple")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="purple")
            buttons[1][column].config(bg="purple")
            buttons[2][column].config(bg="purple")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="purple")
        buttons[1][1].config(bg="purple")
        buttons[2][2].config(bg="purple")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="purple")
        buttons[1][1].config(bg="purple")
        buttons[2][0].config(bg="purple")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="green")
        return "Tie"
    else:
        return False

def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    return spaces != 0

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

def main():
    global label
    # Initialising the Tkinter window
    window = Tk()
    window.title("Tic-Tac-Toe")

    # Creating game widgets
    label = Label(window, text=player + " turn", font=('consolas', 40))
    label.pack(side="top")

    reset_button = Button(window, text="restart", font=('consolas', 20), command=new_game)
    reset_button.pack(side="top")

    frame = Frame(window)
    frame.pack()

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                           command=lambda row=row, column=column: next_turn(row, column))
            buttons[row][column].grid(row=row, column=column)

    # Start the main event loop for the game window
    window.mainloop()

if __name__ == '__main__':
    main()  # Start the Tic Tac Toe game
