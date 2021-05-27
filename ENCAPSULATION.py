# It seems odd that adding the private or protected atb to something dosent realy change how it is used

def ENC1(): #I made them into functions so i could put them at the bottom un needed but i like it this way
    class Protected1:
        def __init__(self):
            self._protectedVar = 369
    obj = Protected1()
    print(obj._protectedVar) # ok so the .protectedVar part makes it print the value stored. or else you get a error? saying that it is protected.
    print(obj)# i added this to see what would happen

        



def ENC2():
    class Protected2:
        def __init__(self):
            self.__privateVar = 963

        def getPrivate(self):
            print(self.__privateVar)


    obj = Protected2() # realy obj is not needed but speeds thing up a bit.
    obj.getPrivate()
    Protected2().getPrivate()# realy obj is not needed but speeds thing up a bit.
    print(obj) # used to show what happens when you dont include .private

if __name__ == "__main__":
    ENC1()
    ENC2()
