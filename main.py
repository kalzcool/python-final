# CC RA KW AB 7th
import sys
# Hangman (python final) 

#CC inputs letters and words

#RA word order

#KW looping the game and lists

#AB conditionals

#CC
game_start = input("would you like to play hangman?\n").strip().title()
#AB
if game_start == "Yes":
    print("Welcome to the game!")
else:
    print("Goodbye!") 
    sys.exit()
    
import random

#RA KW AB CC
words = ["cactus", "cactus"]

#CC 

chosen_word = random.choice(words)
#RA
def hangman():
    chosen_word = random.choice(words)
    random_item_list = list(chosen_word)
    word_length = len(chosen_word)
    display = ["_" ]
    for _ in range(word_length):
        display += "_"
    print(display)
end_of_game = False
lives = 6
#CC
guessed_letters = []
hangman()

def show_words(guessed_letters, lives = 6): 
    guess = input("give me a letter fine sir:\n").lower()
    guessed_letters.append(guess)
#KW
    chosen_word = random.choice(words)
    if guess in chosen_word:
         print(f"You guessed correctly, you have {lives} lives left.")
         
    else:
        lives -= 1
        print(f"You guessed incorrectly, you have {lives} lives left.")
        if lives == 0 :
                print("You loose")
                sys.exit()

   #CC

show_words(guessed_letters)
show_words(guessed_letters, lives = 5)
show_words(guessed_letters, lives = 5)
show_words(guessed_letters, lives = 5)
show_words(guessed_letters, lives = 5)
show_words(guessed_letters, lives = 5)

    