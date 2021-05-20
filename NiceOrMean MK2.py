#
# Python: 39
#
# Author: Josh W
#
# purpose:
#
#



def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        Check if this is a new game or not.
        If it is new get users name
        if it is not a new game thank the player
        for playing agian and continue with the game
    """
    #meaning if we do not already have the users name
    # then they are a new player and we need to get thir name
    if name != "":
        print("\nThankyou for playing agian, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcom, {}!".format(name))
                    print("\nIn this game you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>").lower()
        if pick == "n":
            print("\nThe strange walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name)#pass the 3 var to the score().

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: #if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call win function passing in the variables so it can use them
        lose(nice,mean,name)
    else:  #else call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    # Substitute the {} wildcards with our var values
    print("\nGrats {}, you win!!! \nEveryone loves you \nand you've made alot of friends alon the way".format(name))
    # call agian function and pass in our vars
    again(nice,mean,name)

def lose(nice,mean,name):
    # Substitutes the {} wilde cards with our var values
    print("\nWow {}, you realy suck! \nYou are a terrible person.\nHopefuly you change your ways.".format(name))
    # Now we call the agian function to start the game over if the user wants to
    again(nice,mean,name)

def again(nice,mean,name):
    stop  = True# this stops the loop to ask the question, if yes below it will call a diferent function
    while stop:
        choice = input("\nDo you want to play again? (y/n): \n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)# the function that gets called by the again function
        if choice == "n":
            print("\nOh no sorry to see you leave")
            stop = False
            quit()# This pre function closes the program if conditions are met
        else: # This displayes if the user dosent input a Y or N answer
            print("\nEnter (Y) for 'Yes', (N) for 'No': \n>>>")

def reset(nice,mean,name):
    nice = 0 # This part triggeres if the user decides to play agian
    mean = 0 # It passes the name value back to start and sets nice ane mean to 0
    # We only reset the nice and mean because we already have the users name stored.
    start(nice,mean,name) # This is the start function from the bagining of the program






if __name__ == "__main__":
    start()
