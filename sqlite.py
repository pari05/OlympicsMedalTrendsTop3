#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')

#conn.
print "Opened database successfully", conn.__str__();

#===============================================================================
# /*conn.execute('''CREATE TABLE COMPANY
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')*/
#===============================================================================
#print "Table created successfully";

cursor = conn.execute("select distinct country, count from OlympicsMedalData where year = 2016 and indicator = \'Total\' and country <> \'World\' order by count desc limit 3");
countries = []
medals1 = []
medals2 = []
medals3 = []
years = []
for row in cursor:
   print "country = ", row[0]
   countries.append(row[0])
   print "count = ", row[1], "\n"

cursor = conn.execute("select count from OlympicsMedalData where year <= 2016 and year > 2000 and indicator = \'Total\' and country = \'" + countries[0] + "\' order by year asc");
for row in cursor:
   print "medals = ", row[0]
   medals1.append(row[0])
   

cursor = conn.execute("select year, count from OlympicsMedalData where year <= 2016 and year > 2000 and indicator = \'Total\' and country = \'" + countries[1] + "\' order by year asc");
for row in cursor:
   print "years = ", row[0]
   print "medals = ", row[1]
   years.append(row[0])
   medals2.append(row[1])
   
cursor = conn.execute("select count from OlympicsMedalData where year <= 2016 and year > 2000 and indicator = \'Total\' and country = \'" + countries[2] + "\' order by year asc");
for row in cursor:
   print "medals = ", row[0]
   medals3.append(row[0])
   
conn.close()