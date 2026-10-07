# Math Quiz Game 🧮

A simple Python math quiz game that generates random addition problems and checks the player's answers.

## About the Project

I built this project as part of **CS50's Introduction to Programming with Python** by Harvard University.

The program asks the player to choose a difficulty level from `1` to `3`. Based on the selected level, it generates random addition problems using non-negative integers with the corresponding number of digits.

The player is given 10 math problems to solve. For each question, the player has up to three attempts to enter the correct answer.

If the answer is incorrect or the input is not a number, the program displays `EEE` and asks again. After three incorrect attempts, the correct answer is displayed and the program moves to the next question.

At the end, the player's score is displayed based on the number of correctly answered questions.

## How It Works

The player first chooses a level:

```text
Level: 1
```

The program then generates addition problems based on that level:

```text
6 + 6 = 12
```

If the answer is incorrect, the program displays:

```text
EEE
```

After three incorrect attempts, the correct answer is shown before moving to the next question.

After all 10 questions, the final score is displayed:

```text
Score: 8
```

## What I Practiced

While working on this project, I practiced:

* Creating and using functions
* Using the `random` module
* Generating random integers
* Working with `while` loops
* Using `for` loops
* Handling `ValueError`
* Validating user input
* Using `try` and `except`
* Keeping track of a score
* Working with function parameters and return values

## Technologies

* Python
* `random`

## Course

This project was completed as part of **CS50's Introduction to Programming with Python** by Harvard University.
