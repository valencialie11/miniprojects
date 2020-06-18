def intro():
    print("Enter Your Name:")
    name = input()
    print("Hello, " + name + ". Do you want to a game?")

def choose():
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n', 'nope'}
    #"Curly Braces" are used in Python to define a dictionary. A dictionary is a data structure that maps one value to another - kind of like how an English dictionary maps a word to its definition.

    choice = input().lower()

    if choice in yes:
        print("Okay! Let's Play")
        print("")
        game()
    elif choice in no:
        print("Goodbye! See you next time!")
        exit()
    else:
        print("Please respond with 'yes' or 'no'")
        choose()

def game():
    
