import os
import mysql.connector
from config import host, user, password, database ,hostname


mydb = mysql.connector.connect(
  host= host,
  user= user,
  password= password,
  database= database
)
response = os.system("ping -c 4 " + hostname)

#and then check the response
if response == 0:
  print (hostname , 'is up!')
  mycursor = mydb.cursor()
  val = [hostname]
  sql = "SELECT server, currentstatus FROM vpsde WHERE server = %s ORDER BY id DESC LIMIT 1 "
  mycursor.execute(sql, val)
  #debug = mycursor.fetchall()
  for row in mycursor:
    empl_data = ','.join(row)
    if empl_data == ((hostname) + "," + "down"):
      print ('currentstatus was down but up now')
      #print (debug)
      #print (row)

      mycursor = mydb.cursor()
      sql = "INSERT INTO vpsde (server, currentstatus) VALUES (%s, %s)"
      val = (hostname, "up")
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")

    else:
      print ('currentstatus is up')
      #print (debug)
      #print (row)

else:
  mycursor = mydb.cursor()
  val = [hostname]
  sql = "SELECT server, currentstatus FROM vpsde WHERE server = %s ORDER BY id DESC LIMIT 1 "
  mycursor.execute(sql, val)
  for row in mycursor:
    empl_data = ','.join(row)
    if empl_data == ((hostname) + "," + "down"):
      print ('currentstatus is down')
      #print (row)

    else:
      print ('currentstatus was up but down now')
      #print (row)
      mycursor = mydb.cursor()
      sql = "INSERT INTO vpsde (server, currentstatus) VALUES (%s, %s)"
      val = (hostname, "down")
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
