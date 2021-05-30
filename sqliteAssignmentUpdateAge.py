


import sqlite3

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor() 
    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",(45, 'Luigi', 'Vercotti' ))


