# CC RA KW AB 7th

#Hangman Python Final

#CC inputs letters and words

#RA word order

#KW looping the game and lists, making the code look nice

#AB conditionals

#CC
import sys
import random

word_list = ["milky", "zigzag", "foggy", "mummy", "jolly", "poppy", "giggle", "happily", "fluffy", "halfway", "hedgehog", "kick", "chipmunk", "kabaddi", "clockwork", "lazy", "juicy", "chuckled", "foxglove", "vuvuzela", "plump", "chuck", "fully", "puff", "jacuzzi", "middle", "magnify", "black", "pack", "punch", "publicly", "dumbbell", "hobby", "apply", "quack", "bluebell", "crazy", "block", "puppy", "quiz", "pick", "gulf", "lucky", "clock", "cyborg", "prickly", "clump", "skull", "buzzer", "jugs", "skillful", "cyberpunk", "puzzle", "symbol", "chef", "windmill", "lollipop", "pumpkin", "building", "yolk", "cloud", "wrongly", "blazing", "fury", "clumsy", "pluck", "awful", "church", "yacht", "furlough", "duck", "muddy", "padlock", "flag", "headache", "flapjack", "unhappy", "lifestyle", "globe",  "decided", "cycling", "awkward", "gypsy", "symbols", "hyperlink", "pebble", "club", "baby", "volume", "review", "puzzling", "quickly", "pudding", "daffodil", "maximum", "suck"]
word = random.choice(word_list)
lives = 7
guessed_letters = []
#RA
def display_word():
    display = " _ "
#KW
    for letter in word:
        if letter in guessed_letters: # If a letter is guessed it will display it, but if its not, it will display _. It does this for every letter in the word.
            print(letter, end="") # Printing correctly guessed letter, replacing the _.
        else:            
            print(display, end="") # Printing "_" because the letter hasn't been guessed.
    print(" ")
#RA
def did_guess_all_letters():
#KW
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True
# Start of game loop
#KW
while lives >= 1:
    print(f"You have {lives} lives left.")
    display_word()
    guess = input("Guess a letter - \n").strip().lower()
#AB
    if len(guess) > 1:
        print("Stop wasting my time.")
        sys.exit() 
    guessed_letters.append(guess) #append adds something to a list (We are adding the guess to the list of guessed letters)
    if guess in word:
        print(f"Correct.")
    else:
        lives -= 1
        print(f"Incorrect.")
    if did_guess_all_letters():
        print(f"Congratulations, you won with {lives} lives left!")
        sys.exit()
#CC
print(f"You don't have any more guesses, you lose. The word was {word}")
sys.exit()