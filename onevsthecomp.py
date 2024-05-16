from tkinter import *

# Variables for game setup
players = ["El Humangus", "El Computador"]
xo = ["x", "o"]
player = players[0]  # Ensure the human player starts first
buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
label = None

# Game logic functions
def next_turn(row, column):
    global player

    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:  # Human turn
            buttons[row][column]["text"] = xo[0]
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + "'s turn"))
                computer_move()
            elif check_winner() is True:
                label.config(text=(players[0] + " wins!"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")
        else:  # Computer's turn
            buttons[row][column]["text"] = xo[1]
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + "'s turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins!"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():
    # Check rows
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True
    # Check columns
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            return True
    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    # Check for tie
    if empty_spaces() == []:
        return "Tie"
    
    return False

def empty_spaces():
    empty = []
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] == "":
                empty.append((row, column))
    return empty

def new_game():
    global player
    player = players[0]  # Ensure the human player starts first
    label.config(text=player + "'s turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", state=NORMAL)

def computer_move():
    best_score = -float('inf')
    best_move = None
    for row, column in empty_spaces():
        buttons[row][column]["text"] = xo[1]
        score = minimax(buttons, False)
        buttons[row][column]["text"] = ""
        if score > best_score:
            best_score = score
            best_move = (row, column)
    if best_move:
        next_turn(best_move[0], best_move[1])

def minimax(board, is_maximizing):
    winner = check_winner()
    if winner == True:
        return 1 if player == players[1] else -1
    elif winner == "Tie":
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row, column in empty_spaces():
            board[row][column]["text"] = xo[1]
            score = minimax(board, False)
            board[row][column]["text"] = ""
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row, column in empty_spaces():
            board[row][column]["text"] = xo[0]
            score = minimax(board, True)
            board[row][column]["text"] = ""
            best_score = min(score, best_score)
        return best_score

# Game structure
def main():
    global label
    # Initialize the Tkinter window
    window = Tk()
    window.title("Tic-Tac-Toe")

    # Create game widgets
    label = Label(window, text=player + "'s turn", font=('consolas', 40))
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
