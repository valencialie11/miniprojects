import random

def intro():
    print("Enter Your Name:")
    name = input()
    print("Hello, " + name + ". Do you want to play guess the number?")

def choose():
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n'}
    #"Curly Braces" are used in Python to define a dictionary. A dictionary is a data structure that maps one value to another - kind of like how an English dictionary maps a word to its definition.

    choice = input().lower()

    if choice in yes:
        print("Okay! Let's Play")
        print("We have picked a random number from 1 to 100. Your job is to guess what number we have picked in less than 10 tries! A hint will be given after every wrong answer. Input your first guess below!")
        game()
    elif choice in no:
        print("Goodbye! See you next time!")
        exit()
    else:
        print("Please respond with 'yes' or 'no'")
        choose()

def game():
    num = random.randint(1,101)
    for num0 in range(0,10):
        num0 = int(input())
        if num0 == num:
            print("Congratulations! You have guessed the correct number! Try another round?")
            choose()
        elif num0 < num:
            print("The mystery number is higher than your guess. Try again!")
        elif num0 > num:
            print("The mystery number is lower than your guess. Try again!")
    if num0 != num:
        print("Sorry, you failed this game. Your mystery number is " + str(num) + ". Try another round?")
        choose()
    else:
        print("Congratulations! You have guessed the correct number! Try another round?")
        choose()


if __name__== "__main__":
  intro()
  choose()
  game()