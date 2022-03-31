


import sqlite3

firstName = input("Enter your first name: ")
lastName = input("Enter you last name: ")
age = int(input("Enter you age:"))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', "+ str(age) +")"
    c.execute(line)
