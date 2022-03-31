class User:
    name = "no name provided"
    email = ' '
    password = '8675309'
    accountN = 0
    join_date = ' '
    ''' I created the user class to give all the
        basic things that everyone would need.
        In the begining this is the information
        that would be importent.
    '''
    
class Admin:
    AdminCommands = True
    ENVcontrols = True
    '''The admin class is what i would use to give
    permissions to the GM's. In this case Admin
    commands( ban, rank up/down, mute(dur) ect).
    id have it seperate so that the Admin class
    could be used to make a special user that
    dident appear as a GM. A spy GM if you will.
    '''
    

class Character(User):
    CharacterName = ' '
    CharacterArchtype = ' '
    '''The player class would inherit
    all the peramiters of the user class
    but add a Character name and archtype.
    these would be spacific to the user
    and there could be more that one
    instance of Characters ie one user
    could have several characters.
    '''


class GameMaster(User,Admin):
    GMname = ' ' 
    GMrank = ' '
    ''' The GM class or GameMaster class would be
    the moderators of the game. they would be visible
    as GM's and would have access to admin commands
    from the admin class and also all the information
    from the user class. a user could then have an
    admin account and work with the game but also
    have a character account to play/test. I want
    to add one more class that has user and admin
    but works in the shadows probly a GM account
    that has additional permissions.

    '''
    

    
