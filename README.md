# Hangman_Game
Test your knowledge of Bollywood movies with this fun Hangman game in Python!

## How to Play
1. Run the game by executing the Python script:
    ```bash
    python hangman.py
    ```
2. You will be prompted to guess letters to reveal the name of a Bollywood movie.
3. Enter a single letter when prompted and press Enter.
4. The game will display the current state of the movie name, and if you guess a correct letter, it will be revealed.
5. You have a limited number of attempts to guess the movie. The hangman stick figure will be drawn with each incorrect guess.
6. The game ends when you correctly guess the movie or run out of attempts.

## Hangman Stick Figures
The hangman stick figures represent the number of incorrect attempts. They are displayed as follows:
- First incorrect attempt:
    ```
     ------
     |    |
     |
     |
     |
     |
    ---
    ```

- Second incorrect attempt:
    ```
     ------
     |    |
     |    O
     |
     |
     |
    ---
    ```

...and so on, until the maximum attempts are reached.

