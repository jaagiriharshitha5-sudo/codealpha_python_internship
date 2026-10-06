import random

words = ["python", "computer", "programming", "developer", "coding"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

display = ["_"] * len(word)

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")

while wrong_guesses < max_wrong_guesses and "_" in display:

    print("\nWord:", " ".join(display))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")

if "_" not in display:
    print("\nCongratulations!")
    print("You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)