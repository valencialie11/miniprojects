import random
import csv

def intro():
    print("Enter your name:")
    name = input()
    print("Hello, " + str(name) + ". Are you struggling to come up with the perfect password?")

def choose():
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n', 'nope'}
    #"Curly Braces" are used in Python to define a dictionary. A dictionary is a data structure that maps one value to another - kind of like how an English dictionary maps a word to its definition.

    choice = input().lower()

    if choice in yes:
        print("Worry not! You have come to the right place!")
        passgenerate()
    elif choice in no:
        print("Goodbye! See you next time!")
        exit()
    else:
        print("Please respond with 'yes' or 'no'")
        choose()
    
def passgenerate():
    try:
        print("Enter your desired number of characters for your new password. We recommend >6 for stronger password.")
        nochar = int(input())
        print("Enter your desired number of letters for your new password.")
        noletters = int(input())
        print("Enter your desired number of integers for your new password.")
        print("Ensure that the total number of integers and letters desired tally up to the number of characters desired.")
        nonum = int(input())
    except:
        ValueError
        print("Please make sure to input whole numbers.")
    
    print("Do you want a mixture of both uppercase and lowercase?")
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n', 'nope'}
    
    try:
        mix = str(input().lower())
    except:
        ValueError
        print("Please respond with 'yes' or 'no'")

    numbers = {'1','2','3','4','5','6','7','8','9','0'}
    letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g' 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    uppercases = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    lowercases = {'a', 'b', 'c', 'd', 'e', 'f', 'g' 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

    def intersection(list1, list2):
        return list(set(list1) & set(list2)) 

    for mlist in range(0, 1001):
        words = dict(csv.reader(open("random.csv")))
        #change it into a dictionary
        randWord = random.choice(list(words.keys()))
        #Dictionary keys are iterable but not indexable so u shld alw change it to list before subsetting
        #The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
        pass_word = words[randWord]
        mlist = list(pass_word)


        if len(mlist) == nochar and len(intersection(mlist, numbers)) == nonum and len(intersection(mlist, letters)) == noletters and mix in no:
            print('pass_word')
            print("Here is your password! " + str(pass_word) + ". Unsatisfied with your new password?")
            choose()
            break

        elif len(mlist) == nochar and len(intersection(mlist, numbers)) == nonum and len(intersection(mlist, letters)) == noletters and mix in yes and intersection(mlist, uppercases) and intersection(mlist, lowercases):
            print('pass_word')
            print("Here is your password! " + str(pass_word) + ". Regenerate new password?")
            choose()
            break

    else:
        print("Sorry, no password in our database matched your requirements. Would you like to try again?")
        choose()

if __name__== "__main__":
  intro()
  choose()
  passgenerate()
    



