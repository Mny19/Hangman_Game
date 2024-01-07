import random

def choose_movie():
    movies = ["dangal", "pk", "padmaavat", "sultan", "queen", "baahubali", "chennaiexpress", "3idiots", "raazi", "kabirsingh"]
    return random.choice(movies)

def display_movie(movie, guessed_letters):
    display = ""
    for letter in movie:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def draw_hangman(attempts):
    hangman_graphics = [
        """
         ------
         |    |
         |
         |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |    |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        ---
        """
    ]
    print(hangman_graphics[attempts])

def hangman():
    print("Welcome to Bollywood Movies Hangman!")
    secret_movie = choose_movie()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nAttempts left:", attempts)
        draw_hangman(6 - attempts)  
        current_display = display_movie(secret_movie, guessed_letters)
        print("Current Movie:", current_display)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_movie:
            print("Incorrect guess!")
            attempts -= 1
        else:
            print("Correct guess!")

        if "_" not in display_movie(secret_movie, guessed_letters):
            print("Congratulations! You guessed the movie:", secret_movie)
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The correct movie was:", secret_movie)
        draw_hangman(6)  

if __name__ == "__main__":
    hangman()
