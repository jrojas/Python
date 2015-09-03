# Write a script called "database.py" to print out the cities with the July being the warmest month. Your script must:

# Connect to the database
import sqlite3 as lite
import pandas as pd


con = lite.connect('getting_started.db');



# Create the cities and weather tables (HINT: first pass the statement DROP TABLE IF EXISTS <table_name>; to remove the table before you execute the CREATE TABLE ... statement)
#DROP TABLE IF EXISTS cities;
#CREATE TABLE cities (name text, state text);
#DROP TABLE IF EXISTS weather;
#CREATE TABLE weather (city text, year integer,warm_month text,cold_month text,average_high integer);

#Insert data into the two tables

with con:

    cur = con.cursor()
    
    cur.execute("DROP TABLE IF EXISTS cities;")
    cur.execute("CREATE TABLE cities (name text, state text);")
    cur.execute("INSERT INTO cities VALUES('New York City', 'NY')")
    cur.execute("INSERT INTO cities VALUES('Boston', 'MA')")
    cur.execute("INSERT INTO cities VALUES('Chicago', 'IL')")
    cur.execute("INSERT INTO cities VALUES('Miami', 'FL')")
    cur.execute("INSERT INTO cities VALUES('Dallas', 'TX')")
    cur.execute("INSERT INTO cities VALUES('Seattle', 'WA')")
    cur.execute("INSERT INTO cities VALUES('Portland', 'OR')")
    cur.execute("INSERT INTO cities VALUES('San Francisco', 'CA')")
    cur.execute("INSERT INTO cities VALUES('Los Angeles', 'CA')")
    
    cur.execute("DROP TABLE IF EXISTS weather;")
    cur.execute("CREATE TABLE weather (city text, year integer,warm_month text,cold_month text,average_high integer);")
    cur.execute("INSERT INTO weather VALUES('New York City', 2013, 'July', 'January',62)")
    cur.execute("INSERT INTO weather VALUES('Boston', 2013, 'July', 'January',59)")
    cur.execute("INSERT INTO weather VALUES('Chicago', 2013, 'July', 'January',59)")
    cur.execute("INSERT INTO weather VALUES('Miami', 2013, 'August', 'January',84)")
    cur.execute("INSERT INTO weather VALUES('Dallas', 2013, 'July', 'January',77)")
    cur.execute("INSERT INTO weather VALUES('Seattle', 2013, 'July', 'January',61)")
    cur.execute("INSERT INTO weather VALUES('Portland', 2013, 'July', 'December',62)")
    cur.execute("INSERT INTO weather VALUES('San Francisco', 2013, 'September', 'December',64)")
    cur.execute("INSERT INTO weather VALUES('Los Angeles', 2013, 'September', 'December',62)")


#Join the data together
#Load into a pandas DataFrame
query = "SELECT name, warm_month  FROM cities INNER JOIN weather ON name = city WHERE warm_month = 'July';"
with con:

  cur = con.cursor()
  cur.execute(query)

  rows = cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  df = pd.DataFrame(rows, columns=cols)


#Print out the resulting city and state in a full sentence. For example: "The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA..."

CITY = df['name'];
print "The cities that are warmest in July are:\n %s"% CITY
#Push your code to Github and enter the link below
