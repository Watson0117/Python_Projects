

import sqlite3

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor() 
    c.execute("DELETE FROM People WHERE FirstName= 'Luigi')


