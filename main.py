# A bad version of Wordle written in Python
# WordleSolver @ https://github.com/gs109111/WordleSolver/

# TODO:
# Move everything to a class

# Modules
import random
import requests
from filter_words import *
import tkinter as tk
from tkinter import messagebox
import webbrowser

# Init Variables
word = ""
current_row = 0
selected_word = ""
submitted = False
word_list = ""

# Extra
def website():
    webbrowser.open("https://github.com/gs109111/WordleSolver")

def update_list():
    messagebox.showinfo("Wordle Python", "Updating, Press Ok To Continue...")

    words_list_url = "https://github.com/gs109111/WordleSolver/raw/refs/heads/dictionary/en/words.txt"

    try:
        # Download latest wordlist
        resp = requests.get(words_list_url)

        with open("words.txt", 'wb') as f:
            f.write(resp.content)

        messagebox.showinfo("Wordle Python", "Done!")

    except (requests.ConnectionError, requests.Timeout):
        pass

# Select random word

def select_word():
    global selected_word

    random_word = random.choice(word_list)

    if random_word:
        selected_word = random_word

# Check if word is in wordlist
def is_word_in_dict(word):

    if word in word_list:
        return True
    else:
        return False

# Reset the game
def reset_game():
    global word
    global current_row
    global selected_word
    global submitted

    for row in range(6):
        for col in range(5):
            grid_labels[row][col].config(text="", bg="lightblue")

    word = ""
    current_row = 0
    submitted = False
    select_word()
    update_display()
    win.update_idletasks()
    win.focus_force()

# Update the display
def update_display():

    global selected_word
    global word
    global current_row
    global submitted

    for col, letter in enumerate(word):
        grid_labels[current_row][col].config(text=letter.upper())

        if submitted:
            if letter == selected_word[col]:
                grid_labels[current_row][col].config(bg="seagreen")
            elif letter in selected_word:
                grid_labels[current_row][col].config(bg="gold")
            else:
                grid_labels[current_row][col].config(bg="azure3")

    for col in range(len(word), 5):
        grid_labels[current_row][col].config(text="", bg="lightblue")

    win.focus_force()

# Detect and handle key presses
def on_key_press(event):

    global word
    global current_row
    global submitted
    global selected_word
    
    key_pressed = event.keysym.lower()

    if key_pressed.isalpha() and len(key_pressed) == 1:
        if len(word) < 5:
            word += key_pressed

    elif key_pressed == "backspace":
        word = word[:-1]

    elif key_pressed == "return":
        if len(word) == 5:
            if not is_word_in_dict(word):
                messagebox.showwarning("Wordle Python", "Word not in wordlist!")
                word = ""
                win.focus_force()
                return
            
            submitted = True
            update_display()

            if word == selected_word:
                messagebox.showinfo("Wordle Python", "You Won!")
                reset_game()
                
                return

            if current_row == 5:
                selected_word_fl = selected_word[0].upper()
                selected_word = selected_word_fl + selected_word[1:]
                messagebox.showerror("Wordle Python", f"You Lost!\n\nThe Correct Word Was: {selected_word}")
                
                reset_game()
                return

            current_row += 1
            word = ""
            submitted = False
    else:
        pass
        
    update_display()

# Window gen + menu bar
win = tk.Tk()
win.title(f"Wordle Python v1.0.0")
win.geometry("360x470")

menubar = tk.Menu(win)
win.config(menu=menubar)

file_menu = tk.Menu(menubar)

file_menu.add_command(
    label='Update Wordlist',
    command=update_list
)
file_menu.add_command(
    label='Project Webpage',
    command=website
)

menubar.add_cascade(
    label="Settings",
    menu=file_menu
)

filter_from_wordlist("words.txt")
with open("words_filtered.txt", "r") as f2:
    lines = [line.strip() for line in f2]
    word_list = lines

select_word()

# Board generation

grid_labels = []

# Draw 
for row in range(6):
    row_labels = []
    for col in range(5):
        letter_block = tk.Label(
            win,
            text=" ",
            bg="lightblue",
            font=("Arial", 18),
            width=4,
            height=2
        )

        letter_block.grid(row=row, column=col, padx=5, pady=5)
        row_labels.append(letter_block)

    grid_labels.append(row_labels)

win.bind("<Key>", on_key_press)

# Draw
win.mainloop()





