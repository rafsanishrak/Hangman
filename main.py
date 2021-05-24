import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
print(
    "RULES : A random word will be chosen by the computer, you have to guess all the letters of that chosen word one by one. "
    "If you choose a correct letter, the letter will be revealed in the result and you can continue choosing the other letters. "
    "You can guess wrong as many times as the number of digits the chosen word has. "
    "For each wrong guess you'll see a man is getting stringed up.")
print("\n")
print("\n")

game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    # Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            print("you guessed this one right, try guessing nexts.")
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("\n")
            print("\n")
            print("You lost all your lives, GAME OVER !!!")

    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])