import random
from hangman_words import word_list
import hangman_art


#Randomly select word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#print(chosen_word) #debugging

#setup lives
lives = 6

#Initial art and guesss
print(hangman_art.logo)

#Create display word
display = []

for letter in range (word_length):
    display += "_"
#print(display) 

game_end = False


while game_end == False:
    guess= input("Guess a letter: ").lower()
    #print(guess) debugging
    
    if guess not in display:
        for position in range(word_length):
            if chosen_word[position] == guess:
                # print("Right")
                display[position] = guess
                
            
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives = lives - 1
                
        print(display) #debugging
        print(f"You have {lives} lives left.")
        print(hangman_art.stages[lives])

        if "_" not in display:
            game_end = True
            print("You win!")

        if lives == 0:
            game_end = True
            print("You lose. :(")
    else:
        print (f"You have already guessed {guess}.")



