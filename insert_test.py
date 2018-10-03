#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      KELS
#
# Created:     02/10/2018
# Copyright:   (c) KELS 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(
    host='localhost',
    user='root',
    password='shyzay2007',
    database='topstories'
)

cursor = mariadb_connection.cursor()

#insert information
#cursor.execute("CREATE TABLE Stories (headline VARCHAR(255), publisher VARCHAR(255))")

sql = "INSERT INTO Stories (headline, publisher) VALUES (%s, %s)"
val = [
  ('Juventus sank Young Boys as Dyballa scored a hattrack', 'Ugochukwu Oputa'),
  ('Manchester United form still in doubt as Valencia forced them to a barren draw', 'Victoria Chinda'),
  ('Manchester City narrowly escaped with a 1-2 win in Germany', 'Boffy Udenyi'),
  ('Bayern held to a 1-1 all draw by Ajax', 'Kemfon Abasi'),
  ('Ramos and Bale absent as Real Madrid suffer a 0-1 defeat to CSKA Moscow in Russia', 'Millicent Wokeh'),
  ('Lyon came from 2 goals down, to leveling the game against Sharkter', 'Victor Elemele')
]

cursor.executemany(sql, val)

mariadb_connection.commit()
print(cursor.rowcount, "was inserted.")
