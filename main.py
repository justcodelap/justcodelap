
from bs4 import BeautifulSoup
from posixpath import expanduser
from bs4.element import SoupStrainer
import mysql.connector
from mysql.connector import Error
from typing import Text
import requests
import csv

url = "https://www.cineplex.de/programm/aichach/"
urll = "https://www.cineplex.de/aichach/"
soup = BeautifulSoup(urll, 'html.parser')
ressponse = requests.get(urll)
response = requests.get(url)
htmll = BeautifulSoup(ressponse.text, 'html.parser')
html = BeautifulSoup(response.text, 'html.parser')
quotes_html = htmll.find_all('div', {"class": "title"})
time = htmll.find_all('div', {"class": "date"})
date = htmll.find_all('div', {"class": "time"})
for link in html.find_all('a'):
    print(link.get('href'))

quotes = list()
mydb = mysql.connector.connect(host='localhost',
                               database='filme',
                               user='root',
                               password='')
# for quotes_html in zip(quotes):
for i, j, k in zip(quotes_html, time, date):
    mycursor = mydb.cursor()
    sql = "INSERT INTO sheesh (film, time, date) VALUES (%s, %s, %s)"
    val = (f"{i.get_text()}", f"{j.get_text()}", f"{k.get_text()}")
    mycursor.execute(sql, val)
    print(val)

try:

    mydb.commit()

    print("1 record inserted, ID:", mycursor.lastrowid)

except mysql.connector.Error as error:
    print("Failed to insert record into film table {}".format(error))

finally:
    if mydb.is_connected():
        mydb.close()
        print("MySQL connection is closed")
