
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

word = "apple"

cha = 4


def game(chance):
    guess = input("Guess a letter in the word ")
    if guess in word:
        print("You won")
        new_game = input("Do you want to continue ? press 'y' for yes press any other key for exit : ")
        if new_game.lower() == 'y':
            game(chance)
        else:
            print("Thanks for playing")
    else:
        print(HANGMAN_PICS[4 - chance])
        chance -= 1
        if chance == -1:
            print("HANGMAN")
        else:
            game(chance)


game(cha)
