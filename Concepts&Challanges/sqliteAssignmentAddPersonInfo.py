


import sqlite3

firstName = input("Enter your first name: ")
lastName = input("Enter you last name: ")
age = int(input("Enter you age:"))
personData = (firstName, lastName, age)

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor() 
    c.execute("INSERT INTO People VALUES (?, ?, ?)", personData)


