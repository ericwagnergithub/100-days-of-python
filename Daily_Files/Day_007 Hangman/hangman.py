#Setup word list
word_list = ["aardvark", "baboon", "camel"]

#Randomly select word
import random
chosen_word = random.choice(word_list)
#print(chosen_word) #debugging

#Initial art and guess
print("Hangman ASCII")
guess= input("Guess a letter: ").lower()
#print(guess) debugging

#Create display word
display = []
for letter in range (1,len(chosen_word)+1):
    display += "_"
print(display)

n=0
for letter in chosen_word:
    if letter == guess:
        print("Right")
        display[n] = guess
    else:
        print("Wrong")
    n += 1

print(display) #debugging






