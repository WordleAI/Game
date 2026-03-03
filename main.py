# Wordle written in Python
# WordleSolver 
# https://github.com/gs109111/WordleSolver

# Modules
import random
import requests
from filter_words import *
import tkinter as tk
from tkinter import messagebox
import webbrowser

class WordlePython():
    def __init__(self):
        self.selected_word = ""
        self.current_row = 0
        self.is_submitted = False
        self.word_list = None
        self.words_list_url = "https://github.com/gs109111/WordleSolver/raw/refs/heads/dictionary/en/words.txt"
        self.grid_labels = []
        self.word = ""

        # Window gen + menu bar
        self.win = tk.Tk()
        self.win.title(f"Wordle Python v1.0.0")
        self.win.resizable(False, False) 

        menubar = tk.Menu(self.win)
        self.win.config(menu=menubar)

        settings_menu = tk.Menu(menubar)

        developer_menu = tk.Menu(menubar)

        settings_menu.add_command(
            label='Reset Game',
            command=self.reset_game
        )

        settings_menu.add_command(
            label='Update Wordlist',
            command=self.update_list
        )

        settings_menu.add_separator()

        settings_menu.add_command(
            label='Project Website',
            command=self.website
        )

        menubar.add_cascade(
            label="Settings",
            menu=settings_menu
        )

        developer_menu.add_command(
            label="Get Answer",
            command=self.get_answer
        )

        menubar.add_cascade(
            label="Developer Options",
            menu=developer_menu
        )
        
        try:
            filter_from_wordlist("words.txt")
            with open("words_filtered.txt", "r") as f2:
                lines = [line.strip() for line in f2]
                self.word_list = lines
        except:
            self.update_list()

        self.select_word()

        # Board generation

        # Draw 
        for row in range(6):
            row_labels = []
            for col in range(5):
                letter_block = tk.Label(
                    self.win,
                    text=" ",
                    bg="lightblue",
                    fg="black",
                    font=("Arial", 18),
                    width=4,
                    height=2
                )

                letter_block.grid(row=row, column=col, padx=5, pady=5)
                row_labels.append(letter_block)

            self.grid_labels.append(row_labels)

        self.win.bind("<Key>", self.on_key_press)

        # Draw
        self.win.mainloop()
        


    # Extra
    def website(self):
        webbrowser.open("https://github.com/gs109111/WordleSolver")

    def get_answer(self):
        messagebox.showinfo("Wordle Python", f"Answer: {self.selected_word}")

    def update_list(self):
        messagebox.showinfo("Wordle Python", "Updating Wordlist, Press Ok To Continue...")

        try:
            # Download latest self.wordlist
            resp = requests.get(self.words_list_url)

            with open("words.txt", 'wb') as f:
                f.write(resp.content)
            
            filter_from_wordlist("words.txt")

            messagebox.showinfo("Wordle Python", "Done!")

        except (requests.ConnectionError, requests.Timeout):
            pass

    # Select random word

    def select_word(self):
        random_word = random.choice(self.word_list)

        if random_word:
            self.selected_word = random_word

    # Check if word is in wordlist
    def is_word_in_dict(self, word):

        if self.word in self.word_list:
            return True
        else:
            return False

    # Reset the game
    def reset_game(self):

        for row in range(6):
            for col in range(5):
                self.grid_labels[row][col].config(text="", bg="lightblue")

        self.word = ""
        self.current_row = 0
        self.is_submitted = False
        self.select_word()
        self.update_display()
        self.win.update_idletasks()
        self.win.focus_force()

    # Update the display
    def update_display(self):

        for col, letter in enumerate(self.word):
            self.grid_labels[self.current_row][col].config(text=letter.upper())

            if self.is_submitted:
                if letter == self.selected_word[col]:
                    self.grid_labels[self.current_row][col].config(bg="seagreen")
                elif letter in self.selected_word:
                    self.grid_labels[self.current_row][col].config(bg="gold")
                else:
                   self.grid_labels[self.current_row][col].config(bg="azure3")

        for col in range(len(self.word), 5):
            self.grid_labels[self.current_row][col].config(text="", bg="lightblue")

        self.win.focus_force()

    # Detect and handle key presses
    def on_key_press(self, event):
        
        key_pressed = event.keysym.lower()

        if key_pressed.isalpha() and len(key_pressed) == 1:
            if len(self.word) < 5:
                self.word += key_pressed

        elif key_pressed == "backspace":
            self.word = self.word[:-1]

        elif key_pressed == "return":
            if len(self.word) == 5:
                if not self.is_word_in_dict(self.word):
                    messagebox.showwarning("Wordle Python", "Word not in wordlist!")
                    self.word = ""
                    self.win.focus_force()
                    return
                
                self.is_submitted = True
                self.update_display()

                if self.word == self.selected_word:
                    messagebox.showinfo("Wordle Python", "You Won!")
                    self.reset_game()
                    
                    return

                if self.current_row == 5:
                    selected_word_fl = self.selected_word[0].upper()
                    self.selected_word = selected_word_fl + self.selected_word[1:]
                    messagebox.showerror("Wordle Python", f"You Lost!\n\nThe Correct Word Was: {self.selected_word}")
                    
                    self.reset_game()
                    return

                self.current_row += 1
                self.word = ""
                self.is_submitted = False
        else:
            pass
            
        self.update_display()


game = WordlePython()
