import random


HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ---
     ---''', '''
  +---+
  0   |
  |   |
      |
     ---
     ---''', '''
   +---+
   0   |
   |   |
  / \  |
      ---
      ---''', '''
  +---+
  0   |
  |   |
 /|\  |
     ---
     ---''', '''
  +---+
  0   |
  |   |
 /|\  |
 / \ ---
     ---
   ''']

file_path = "/home/cybrosys/Desktop/myFile.txt"  # Replace with the actual file path


def select_random_word(file_name):
    with open(file_name, "r") as file:

        words = file.read().split()

        return random.choice(words)


word_un_stripped = select_random_word(file_path)

word = word_un_stripped.strip("'.?!,").lower()

turns = 4


def game(chance):
    guesses = ''
    print("The word is : " + word)
    while chance > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end="")
            else:
                print("_", end="")
                failed += 1
        if failed == 0:
            print("\nYou won")
            break
        already_guessed = []

        guess = input("\nguess a character of the system generated file : ")
        # input should be one letter
        if len(guess) > 1:
            print("Enter only one letter")
            continue

        guesses += guess
        # Don't repeat the letter
        count = 0
        for i in guesses:
            if i == guess:
                count += 1
       #  print(count)

        if count > 1:
            print("you already entered that letter")
            continue

        if guess not in word:
            chance -= 1
            print("\nWrong")

            print(HANGMAN_PICS[4 - chance])
            print("\nYou have", + chance, 'more guesses')
            if chance == 0:
                print("HANGMAN")
                print("The word is : " + word)


game(turns)
