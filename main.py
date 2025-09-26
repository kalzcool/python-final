# CC RA KW AB 7th
import sys
# Hangman (python final) 

#CC inputs letters and words

#RA word order

#KW looping the game and lists
#CC
game_start = input("would you like to play hangman?\n").strip().title()
#AB
if game_start == "Yes":
    print("Welcome to the game!")
else:
    print("Goodbye!") 
    sys.exit()
    
import random

words = ["cactus", "potato", "butter", "rabbit", "bikini", "cobweb", "absurd", "zombie"]


random_item = random.choice(words)

def hangman():
    print("oogie boogie")

def show_word