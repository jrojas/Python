# The sqlite3 module is used to work with the SQLite database.
import sqlite3 as lite


# Here you connect to the database. The `connect()` method returns a connection object.
con = lite.connect('getting_started.db')

with con:
  # From the connection, you get a cursor object. The cursor is what goes over the records that result from a query.
  cur = con.cursor()  
  cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
  cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
  cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January')")
  cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January')")