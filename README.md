# WordleSolver

This project includes two implementations: a Python version and a C++ port. While both share the same core goal, their features differ slightly. The long-term objective is to move away from reliance on the NYTimes endpoint and other services, focusing on a universal, independent Wordle-solving solution.

#### C++ Solver: https://github.com/gs109111/WordleSolver/tree/solver_cpp
#### Python Solver:  https://github.com/gs109111/WordleSolver/tree/solver_python
#### Dictionary:  https://github.com/gs109111/WordleSolver/tree/dictionary
#### Wordle Python (Game):  https://github.com/gs109111/WordleSolver/tree/game

---

## Game/Testbench (Wordle Python)

A Wordle clone written in Python using Tkinter.

The game follows standard Wordle rules:
- 6 attempts to guess a 5-letter word
- Green: correct letter in the correct position
- Yellow: correct letter in the wrong position
- Gray: letter not in the word

Words are selected randomly from a filtered word list, and guesses are validated against the same wordlist.

The game resets automatically after a win or loss.

---


## External Dependencies
#### Python
- Requests (https://pypi.org/project/requests/)
---

## Todo

| Feature                          | Notes |
|----------------------------------|-------|
| Fix WordlePython class to make it cleaner and better | |
