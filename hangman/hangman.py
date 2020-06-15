import random
import csv

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
    correctAnswer = words[randWord]
    #Subset the dictionary using keys
    
    #A list is an ordered sequence of objects, whereas dictionaries are unordered sets. 
    #However, the main difference is that items in dictionaries are accessed via keys and not via their position, unlike list

    #Dictionary
    #D = {"list":"Liste", "dictionary":"Wörterbuch", "function":"Funktion"}
    #List
    #L = [("list","Liste"), ("dictionary","Wörterbuch"), ("function","Funktion")]

    def split(word): 
        return [char for char in word] 
        #Make a new function to split the word into letters
        
    num = len(split(correctAnswer))
    print("_ "*num)
    input().lower()





if __name__== "__main__":
  intro()
  choose()
  game()
    
    
