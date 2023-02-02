'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''
def hangman_game(
    word, wrong,
    remainder, 
    used_letters):
        while wrong < 6:
            print("\n")
            message = "Guess a letter: "
            guess = input(message)
            if guess in remainder:
                used_letters.add(guess)
                remainder.remove(guess)
                print("You have", 6 - wrong, "tries left.")
                print("Used letters: ", " ".join(used_letters))
                new_word = "".join([letter if letter in used_letters else "_" for letter in word])
                print("Word: ", new_word)
                if "_" not in new_word:
                    print("You guessed the word", word, "!")
                    return
        else:
            wrong = wrong + 1
            new = 6 - wrong
            print("You have", {new}, "tries left.")
            print("Used letters: ", " ".join(used_letters))
            new_word = "".join([letter if letter in used_letters else "_" for letter in word])
            print("Word: ", new_word)
        print("You lost! The word was", word)

def start_game(word):
    word = word.lower()
    wrong = 0
    remainder = set(word)
    used_letters = set()
    hangman_game(word, wrong, remainder, used_letters)

start_game("java")

