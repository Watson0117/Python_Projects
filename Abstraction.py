




from abc import ABC, abstractmethod


class Character(ABC): # this should set Character as an abstract base class
    def BeginingLVL(self, amount):
        print("You enter the world as a level: ",amount)

    @abstractmethod
    def levelUp(self, amount):
        pass


class GainXP(Character):
# this will define howw to implement the levelUp function from its parent BeginingLVL class
    def levelUP(self, amount):
        print("You have gained {} level(s) you are getting more powerfull!".format(amount))

T = GainXP()      
T.BeginingLVL("1")
T.levelUp("1")
        
