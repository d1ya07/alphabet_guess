import random
import string

def alphabet_guessing_game():
    alphabet = list(string.ascii_lowercase)
    secret_letter = random.choice(alphabet)
    attempts = 0

    print("🎯 Welcome to the Alphabet Guessing Game!")
    print("Guess the secret letter (a-z). Type 'exit' to quit.\n")

    while True:
        guess = input("👉 Your guess: ").lower()
        attempts += 1

        if guess == 'exit':
            print("👋 Game exited. Thanks for playing!")
            break

        if len(guess) != 1 or guess not in alphabet:
            print("⚠️ Please enter a valid single letter (a-z).")
            continue

        if guess == secret_letter:
            print(f"🎉 Correct! The letter was '{secret_letter}'. You guessed it in {attempts} tries.")
            break
        elif guess < secret_letter:
            print("🔼 The letter comes after your guess.")
        else:
            print("🔽 The letter comes before your guess.")

# Run the game
alphabet_guessing_game()
