def intro():
    global name
    print("Enter Your Name:")
    name = input()
    print("Hello, " + name + ". Do you want to play a nerve-wrecking yet addictive text-based game?")

def choose():
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n', 'nope'}
    #"Curly Braces" are used in Python to define a dictionary. A dictionary is a data structure that maps one value to another - kind of like how an English dictionary maps a word to its definition.

    choice = input().lower()

    if choice in yes:
        print("Okay! Let's Play")
        print("")
        firstsegment()
    elif choice in no:
        print("Goodbye! See you next time!")
        exit()
    else:
        print("Please respond with 'yes' or 'no'")
        choose()

def firstsegment():
    print("Welcome to Karen M. McManus' book: 'One Of Us Is Lying' inspired text-based game.")
    print("Made by: Valencia Lie")
    print("--------------------- INITIALISING GAME ----------------------")
    print("Hi, " + name + ". You are currently a student in Bayview High School. Mr Avery, your Chemistry teacher, just confiscated a phone in your bag. You are then sent to detention.")
    print("As you enter the detention room, you see 5 different students. Bronwyn Rojas, the smartest girl in school. Addy Prentis, one of the school's prettiest and most popular girl. Nate Macauley, the drug addict of the school. Cooper Clay, the best baseball player in school. And Simon Kelleher, the notorious guy behind ABOUT THAT magazine.")
    print("You are shocked at the strange combination of people in the room. What do you do next?")
    print("1. You sit quietly at the corner of the room and started to wait for Mr Avery to tell you what to do.")
    print("2. You yell out of frustration because the phone Mr Avery found is not yours.")
    print("3. You head towards one of the students and ask whether this is a mistake.")
    try:
        firstchoice = int(input())
    except ValueError:
        print("Please enter just the number (1,2 or 3) of your choice.")
    
    if firstchoice == 1:
        avery = print("Suddenly, Mr Avery came. He handed each person a paper and asked everyone to write 500 essay on the negative impacts of technology on teens in America. What would you do next?")
    elif firstchoice == 2:
        print('"AAAAAAHHHH!!" you shouted. The other 5 people looked at you strangely and started asking you who you are. Apparently, they have never even known your existence before. What do you do next?')
        print("1. Introduce your name.")
        print('2. Say incredulously, "How is it that you guys dont know who I am?"')
        print("3. Ignore their question.")
        try:
            action = int(input())
        except ValueError:
            print("Please enter just the number (1, 2, 3, 4 or 5) of your choice.")
        if action == 1:
            print("My name is " + name + ". Nice to meet you guys, I guess. I've been here since freshman though...")
            avery
        elif action == 2:
            print('They rolled their eyes and said, "How are we supposed to know you when youre as mute as a mouse?!"')
            avery
        else:
            avery
    else:
        print("Who do you ask among the 5 people?")
        print("1. Bronwyn Rojas")
        print("2. Addy Prentiss")
        print("3. Nate Macauley")
        print("4. Cooper Clay")
        print("5. Simon Kelleher")
        try:
            who = int(input())
        except ValueError:
            print("Please enter just the number (1, 2, 3, 4 or 5) of your choice.")
        
        if who == 1:
            print('"Do I look like I purposely bring a phone to Mr Averys class too? Im not dumb. Of course this is a mistake!", says Bronwyn.')
            avery
        elif who == 2:
            print('"I think so. Im supposed to go and see my boyfriend Jake after class. Dang it Mr Avery!", says Addy.')
            avery
        elif who == 3:
            print('"Ya. Im busy enough with my customers and I dont need this kind of bs."')
            avery
        elif who == 4:
            print('"Yes. Its not my phone either. We gotta tell Mr Avery!"')
            avery
        else:
            print('"Duh! I will make sure to feature Mr Avery on ABOUT THAT and make him pay!"')
            avery






    
