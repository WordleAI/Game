# WordleSolver

This project includes two implementations: a Python version and a C++ port. While both share the same core goal, their features differ slightly. The long-term objective is to move away from reliance on the NYTimes endpoint and other services, focusing on a universal, independent Wordle-solving solution.

#### C++ Version: https://github.com/gs109111/WordleSolver/tree/cpp
#### Python Version:  https://github.com/gs109111/WordleSolver/tree/python

---

## Game (Wordle Python)

A Wordle clone written in Python using Tkinter.

The game follows standard Wordle rules:
- 6 attempts to guess a 5-letter word
- Green: correct letter in the correct position
- Yellow: correct letter in the wrong position
- Gray: letter not in the word

Words are selected randomly from a filtered word list, and guesses are validated against the same dictionary.

The game resets automatically after a win or loss.

---

## Todo

| Feature                          | Notes |
|----------------------------------|-------|
| Move everything to a class | |

