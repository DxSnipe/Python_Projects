import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = [
  '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

end_of_game = False
lives = 6

word_list = [
  "ardvark", "baboon", "camel", "august", "september", "apple", "umbrella",
  "hello", "tomorrow", "fuzzy", "brook", "repeated", "english", "hahahaha",
  "unscramble", "repeat", "possible", "double", "number", "letter",
  "dictionary", "hangman", "unique", "best"
]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)
#print(f'Pssst, the solution is {chosen_word}.')
print(
  "\nGuess a letter and keep completing the word!! \nYou have 6 lives to answer correctly before you get hanged. \nIf you guess wrong letter 6 times, you will be hanged and Game Over!!\n"
)

display = []
for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"You've already guessed {guess}")

  for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print(f"\nYou lose.\nThe correct word is '{chosen_word}'")

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win.")

  print(stages[lives])
