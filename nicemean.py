#
# Python: 3.7.8
#
# Author: Brian Brown
#
# Purpose: The Tech Academy Python course tutorial for Mean or Nice Game
#               Demonstrating how tgo pass vars from function
#               to function while producing a fucntional game.
#
#               Remember, function_name(variable) means that we pass in the var.
#               Return var means that we are returning the variable back to the
#               calling function.


def start(nice=0,mean=0,name=""):
    # get user's info
    name = describeGame(name)
    nice,mean,name = niceMean(nice,mean,name)
    

def describeGame(name):
    """
        Check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game.
    """
    #meaning, if we do not already have this user's name,
    #then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def niceMean(nice,mean,name):
    stop = True
    while stop:
        showScore(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe person glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the 3 vars to the score()


def showScore(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    #score function is being passed the values stored within the 3 vars
    if nice > 2:   # if condition is valid, call win function passing in the vars so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the vars so it can use them
        lose(nice,mean,name)
    else:             # else, call niceMean function passing in the vars so it can use them
        niceMean(nice,mean,name)

def win(nice,mean,name):
    # sub the {} wildcards with our var values
    print("\nNice job {}, you win! \nEveryone loves you and you've made lots of friends along the way!".format(name))
    # call again function and pass in our vars
    again(nice,mean,name)


def lose(nice,mean,name):
    # sub the {} wildcards with our var values
    print("\nWow... you are a real jerk and everyone hates you!".format(name))
    # call again function and pass in our vars
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n)\n>>> ").lower()
        if choice == "y":
            print("\n NICE!, Let's do this!")
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES' or ( N ) for 'NO':\n>>> ")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Notice, i do not reset the name var since the user as elected to play again
    start(nice,mean,name)


    



if __name__ == "__main__":
    start()
