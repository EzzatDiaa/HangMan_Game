# programming hangman game

# first step is to make a list of words and then make the programming
# pick form it randomly
import random
from hangman_words import word_list
from hangman_art import logo
print(logo)

len_list = random.randint(0, len(word_list) - 1)
random_word = word_list[len_list]
end_of_the_game = False
lives = 6
print(random_word)
# create a list that contains "-" as length as random_word
display = []
for i in random_word:
    display.append("-")

while not end_of_the_game:
    # second step is to asl the user to guess a letter in a word
    guess_letter = input("Guess a letter in the word:").lower()

    if guess_letter in display:
        print(f"You have already guessed{guess_letter}")

    # third step is to check if the guess_letter in random_word's letters
    for position in range(0, len(random_word)):
        if random_word[position] == guess_letter:
            display[position] = guess_letter
    if guess_letter not in random_word:
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_the_game = True
            print("You lose")
    # join all to make sting
    print(f"{''.join(display)}")

    if "-" not in display:
        end_of_the_game = True
        print("You win")


    from hangman_art import stages
    print(stages[lives])
