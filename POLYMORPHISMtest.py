'''
Create two classes that inherit from another class.
Each child should have at least two of their own attributes.
The parent class should have at least one method (function).
Both child classes should utilize polymorphism on the parent class method.
Add comments throughout your Python explaining your code.
Upload your code to GitHub and submit your link below.  '''

# parent class
class User: #here i create the use clas that will act as the parrent class
    name = 'Vlad'
    password = 'Therussian'

    def getLoginInfo(self): #set basic get login info function up.
        entry_name = input("Enter your name:")  # name and password will be universal
        entry_password = input("Enter your password")
        if (entry_name == self.name and entry_password == self.password): #if the name and password match do the following
            print("Welcom back, {}.".format(entry_name))
        else:
            print("Invalid Entry")

        ''' This is where i make the basic get login info function if i were
    to use this further i dont think User.getLoginInfo would be used
    as i would think that you would have to choose customer or employee first befor loging in.
    id have this right after the function name but it kept sayinf unexpected indent. '''

# child class 1
class Employee(User):
    store_number = '1' # this sets the store number so the input has something to compare it to.
    employee_number = '1' # I wanted to make the text say "welcome employee #1 but that is not in the function and it wouldent let me add it without an input"
    def getLoginInfo(self):
        entry_name = input("Enter your name:")
        entry_password = input("Enter your password")
        entry_storeN = input("Enter store number:")
        if (entry_name == self.name and entry_password == self.password and entry_storeN == self.store_number): # if name password and store number are all correct do this
            print("Welcom back {}, store {} is luck to have you.".format(entry_name,entry_storeN))
        else:
            print("Invalid Entry")

# child class 2
class Customer(User):
    customerID = '2'
    rewardsMember = True # I wanted to make this a condition to get a discount but in dont know how to get the login function to recognise it yet.

    def getLoginInfo(self):
        entry_name = input("Enter your name:")
        entry_password = input("Enter your password")
        entry_customerID = input("Enter your Customer ID:")
        if (entry_name == self.name and entry_password == self.password and entry_customerID == self.customerID): #if name pass and ID are all correct do this
            print("Welcom back, {}.\nHow may we assist you today?.".format(entry_name))
        else:
            print("Invalid Entry")
'''
Each getLoginInfo() function esential dose the same thing but with
this setup it seperates the two into managable groups. The messages
that are displayed are relevant to who logged in. Vlad could login
as a customer or employee dependin on the information put in. 
'''


if __name__ == "__main__":
    CU = User()
    CU.getLoginInfo()
    
    CE = Employee()
    CE.getLoginInfo()

    CC = Customer()
    CC.getLoginInfo()
