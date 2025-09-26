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
words = ["cactus", "potato", "butter", "rabbit", "bikini", "cobweb", "absurd", "zombie", "bagpipes", "pneumonia", "knapsack", "jukebox", "syndrome", "unworthy",  "grogginess", "jawbreaker", "kilobyte", "fishhook", "beekeeper"]

#CC 
random_item = random.choice(words)

#RA
def hangman():
    word = random_item
    random_item_list = list(random_item)
    word_length = len(word)
    display = []
    for _ in range(word_length):
        display += "_"
    print(display)
end_of_game = False
lives = 6
guessed_letters = []
hangman()
def show_words():
    guess = input("give me a letter fine sir:").lower()
#KW
    for letter in words:
        if guess == letter:
            print(f"You guessed correctly, you have {lives} lives left.")
            break
        else:
            print(f"You guessed incorrectly, you have {lives} lives left.")
        lives -= 1
        if lives == 0:
            print("You loose")
            sys.exit()

   # if guess 
show_words()
    