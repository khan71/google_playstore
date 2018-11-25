from bs4 import BeautifulSoup   #from the bs4 package of python import BeautifulSoup library
import requests   #import the package requests which is an HTTP library to ping a website or portal for information
import pymysql   #import PyMySQL which is a pure-Python MySQL client library

conn=pymysql.connect(host='127.0.0.1',port=3307,user='root',password='8793',db='task2')   #declaring a variable 'conn' which used to eastablish the connection with mysql using the arguments user(username) and password to authenticate, db for the database name to use when connecting with the MySQL server, the host name of the MySQL server and the TCP/IP port of the MySQL server which must be an integer.
a=conn.cursor()   #creating a cursor object as it allows python to execute sql commands in database session. declaring a variable 'a' that will execute conn.cursor()

source=requests.get('https://en.softonic.com/solutions/what-are-the-best-android-apps-for-chatting-with-strangers-anonymously').text   #declaring a variable 'source' to get the source code of the website using the requests library (requests.get() returns a response object). (.text at the end is used to get the source code from the response object). 

soup=BeautifulSoup(source,'lxml')   #declaring a variable 'soup' which is used to pass the html file to the BeautifulSoup library along with the parser. 'lxml' is the parser

atags=soup.find_all('a',class_='card-solution__title')   #declaring a variable 'atags' to get the information from the tags. using find() we can pass in arguments of attributes and is used to find the exact tag that we are looking for. find_all() returns the list of all the tags that matchesthese arguments. (find_all() to search for all the tags 'a' with the class='card-solution__title')
print('1st for loop for url')   #to print('1st for loop for url')
for atag in atags:   #for loop to loop through the list that the variable 'atags' returns 
    url=atag.get('href')   #declaring a variable 'url' to get the 'href' attribute of the tag 'atag'
    print(url)   #to print the value in the variable 'url' viz the 'href' attribute of the 'atag'
    sql="INSERT INTO url (href) VALUES ('%s')" %(url)   #declaring a variable 'sql' and writing a query which will insert the value of the 'url' variable, in the column 'href' of the table 'url'
    a.execute(sql)   #using the execute() of the cursor object to execute the query specified in the 'sql' variable
    conn.commit()   #as the program completed executing the query, calling the commit() to commit the changes to the database  
    print()   #to print a blank line

print('2nd for loop for rank')   #to print('2nd for loop for rank') 
for atag in atags:   #for loop to loop through the list that the variable 'atags' returns 
    rank=atag.h2.span.text   #declaring a variable 'rank' to get the text of the tag 'span' which is a tag in 'h2' which is a tag in 'atag'
    print(rank)   #to print the value in the variable 'rank' viz the text attribute of the 'atag.h2.span'
    sql="INSERT INTO apprank (rank_id) VALUES ('%s')" %(rank)   #declaring a variable 'sql' and writing a query which will insert the value of the 'rank' variable, in the column 'rank_id' of the table 'apprank'
    a.execute(sql)   #using the execute() of the cursor object to execute the query specified in the 'sql' variable
    conn.commit()   #as the program completed executing the query, calling the commit() to commit the changes to the database     
    print()   #to print a blank line
    
print('3rd for loop for applcation name')   #to print('3rd for loop for application name') 
for atag in atags:   #for loop to loop through the list that the variable 'atags' returns 
    appname = atag.h2.text   #declaring a variable 'appname' to get the text of the tag 'h2' which is a tag in 'atag'
    rank=atag.h2.span.text   #declaring a variable 'rank' to get the text of the tag 'span' which is a tag in 'h2' which is a tag in 'atag'
    appname = appname.replace(rank,'')   #in this method the rank is replaced by a blank space and just the name of the application is stored in the variable 'appname'
    print(appname)   #to print the value in the variable 'appname' viz the text attribute of the 'atag.h2' and the rank is replaced by a blank space
    sql="INSERT INTO appname (application_name) VALUES ('%s')" %(appname)   #declaring a variable 'sql' and writing a query which will insert the value of the 'appname' variable, in the column 'application_name' of the table 'appname'
    a.execute(sql)   #using the execute() of the cursor object to execute the query specified in the 'sql' variable
    conn.commit()   #as the program completed executing the query, calling the commit() to commit the changes to the database         
    print()   #to print a blank line