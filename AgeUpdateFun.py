


import sqlite3

with sqlite3.connect('test_database.db') as connection:
    FirstName= input("This will modify the age of specified person\nWhat is the first name of the person?")
    LastName= input("What is the last name of the person")
    Age= input("what is the new age?")
    
    c = connection.cursor() 
    c.execute("UPDATE People SET Age={} WHERE FirstName={} AND LastName={}".format(Age, FirstName, LastName ))

