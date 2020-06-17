import random
import csv

def hangman(winning_word,char_guessed):
    for i in winning_word: #For every letter in the winning word
        if i in char_guessed:
            print(f' {i} ' , end='') #Every character guessed will reveal itself 
        else:
            print(' __ ', end='') #Whereas if not then a _ will be presented
    print()

def over(winning_word,char_guessed):
    char_guessed is winning_word

def intro():
    print("Enter your name:")
    name = input()
    print("Hello, " + name + "! Do you want to play Hangman?")

def choose():
    yes = {'yes', 'ye', '', 'y', 'ya'}
    no = {'no', 'nope', 'n'}
    choice = input().lower()

    if choice in yes:
        print("Okay! Let's start the game!")
        print("We have picked a mystery word and you have to guess all the letters before 6 tries. Input a letter:")
        game()
    elif choice in no:
        print("Goodbye! See you next time!")
        exit()
    else:
        print("Please respond with 'yes' or 'no'")
        choose()

def game():
    words = dict(csv.reader(open("randomwords.csv")))
    #change it into a dictionary
    randWord = random.choice(list(words.keys()))
    #Dictionary keys are iterable but not indexable so u shld alw change it to list before subsetting
    #The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
    winning_word = words[randWord]
    #Subset the dictionary using keys
    char_guessed = ''
    
    #A list is an ordered sequence of objects, whereas dictionaries are unordered sets. 
    #However, the main difference is that items in dictionaries are accessed via keys and not via their position, unlike list

    #Dictionary
    #D = {"list":"Liste", "dictionary":"Wörterbuch", "function":"Funktion"}
    #List
    #L = [("list","Liste"), ("dictionary","Wörterbuch"), ("function","Funktion")]
    for inputation in range(0,6):
        inputation = input().lower()
        if inputation not in winning_word:
            print("Sorry, the mystery word does not consist the above input. Try again!")
            hangman(winning_word,char_guessed)
            inputation
        
        elif inputation in char_guessed:
            print("The above letter is guessed already, pick another letter!")
            hangman(winning_word,char_guessed)
            inputation
        
        elif (inputation in winning_word) and (inputation not in char_guessed):
            print("Yes! The above letter exists in the mystery word. Input another letter!")
            char_guessed += inputation
            hangman(winning_word,char_guessed)
            inputation
            if over(winning_word,char_guessed):
                print("Congratulations, you have guessed the mystery word! Would you like to try again?")
                choose()
            else:
                print("Sorry, you have failed this round. The mystery word is " + str(winning_word)+ ". Would you like to try again?")
                choose()

if __name__== "__main__":
  intro()
  choose()
  game()
    
    
