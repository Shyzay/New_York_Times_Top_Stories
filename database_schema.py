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
    password='shyzay2007'
)

cursor = mariadb_connection.cursor()

cursor.execute("CREATE DATABASE topstories")




