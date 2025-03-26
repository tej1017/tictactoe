import tkinter as tk
from tkinter import messagebox

def check_win(state):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for w in wins:
        if sum(state[0][i] for i in w) == 3: return "X"
        if sum(state[1][i] for i in w) == 3: return "O"
    return "Draw" if sum(state[0]) + sum(state[1]) == 9 else None

def on_click(index):
    global turn, state, buttons
    if state[0][index] or state[1][index]:
        return
    
    state[turn][index] = 1
    buttons[index].config(text="X" if turn == 0 else "O", state=tk.DISABLED)
    winner = check_win(state)
    if winner:
        messagebox.showinfo("Game Over", "It's a draw!" if winner == "Draw" else f"{winner} wins!")
        reset_game()
    else:
        turn = 1 - turn
        status_label.config(text=f"{'X' if turn == 0 else 'O'}'s Turn")

def reset_game():
    global state, turn, buttons
    state = [[0]*9, [0]*9]
    turn = 0
    for btn in buttons:
        btn.config(text="", state=tk.NORMAL)
    status_label.config(text="X's Turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

state = [[0]*9, [0]*9]
turn = 0

status_label = tk.Label(root, text="X's Turn", font=("Arial", 14))
status_label.pack()

frame = tk.Frame(root)
frame.pack()

buttons = []
for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2, command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

reset_btn = tk.Button(root, text="Reset", font=("Arial", 12), command=reset_game)
reset_btn.pack()

root.mainloop()
