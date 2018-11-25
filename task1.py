from bs4 import BeautifulSoup   #from the bs4 package of python import BeautifulSoup library
import requests   #import the package requests which is an HTTP library to ping a website or portal for information
import pymysql   #import PyMySQL which is a pure-Python MySQL client library

conn=pymysql.connect(host='127.0.0.1',port=3307,user='root',password='8793',db='playstore')   #declaring a variable 'conn' which used to eastablish the connection with mysql using the arguments user(username) and password to authenticate, db for the database name to use when connecting with the MySQL server, the host name of the MySQL server and the TCP/IP port of the MySQL server which must be an integer.
a=conn.cursor()   #creating a cursor object as it allows python to execute sql commands in database session. declaring a variable 'a' that will execute conn.cursor()

source=requests.get('https://play.google.com/store/apps').text   #declaring a variable 'source' to get the source code of the website using the requests library (requests.get() returns a response object). (.text at the end is used to get the source code from the response object). 

soup=BeautifulSoup(source,'lxml')   #declaring a variable 'soup' which is used to pass the html file to the BeautifulSoup library along with the parser. 'lxml' is the parser
   
titles=soup.find_all('a',class_='title')   #declaring a variable 'titles' to get the information from the tags. using find() we can pass in arguments of attributes and is used to find the exact tag that we are looking for. find_all() returns the list of all the tags that matchesthese arguments. (find_all() to search for all the tags 'a' with the class='title')
print('1st for loop URL of the Application:')   #to print('1st for loop for URL of the Application')
for title in titles:   #for loop to loop through the list that the variable 'titles' returns 
    url=title.get('href')   #declaring a variable 'url' to get the 'href' attribute of 'title'
    print(url)   #to print the value in the variable 'url' viz the 'href' attribute of 'title'
    sql="INSERT INTO url (href) VALUES ('%s')" %(url)   #declaring a variable 'sql' and writing a query which will insert the value of the 'url' variable, in the column 'href' of the table 'url'
    a.execute(sql)   #using the execute() of the cursor object to execute the query specified in the 'sql' variable
    conn.commit()   #as the program completed executing the query, calling the commit() to commit the changes to the database
    print()   #to print a blank line
    
print('2nd for loop Application Name:')   #to print('2nd for loop for Application Name')
for title in titles:   #for loop to loop through the list that the variable 'titles' returns 
    appname=title.text   #declaring a variable 'appname' to get the text attribute of 'title'
    print(appname)   #to print the value in the variable 'appname' viz the text attribute of 'title'
    sql="INSERT INTO appname (application_name) VALUES ('%s')" %(appname)   #declaring a variable 'sql' and writing a query which will insert the value of the 'appname' variable, in the column 'application_name' of the table 'appname'
    a.execute(sql)   #using the execute() of the cursor object to execute the query specified in the 'sql' variable
    conn.commit()   #as the program completed executing the query, calling the commit() to commit the changes to the database
    print()   #to print a blank line
    
docidnames=soup.find_all('div',class_='card no-rationale square-cover apps small')   #declaring a variable 'docidnames' to get the information from the tags. using find() we can pass in arguments of attributes and is used to find the exact tag that we are looking for. find_all() returns the list of all the tags that matchesthese arguments. (find_all() to search for all the tags 'div' with the class='card no-rationale square-cover apps small')
print('3rd for loop Doc Id of the Application:')   #to print('3rd for loop for Doc Id of the Application')
for cardrationale in docidnames:   #for loop to loop through the list that the variable 'docidnames' returns 
    docid=cardrationale.get('data-docid')   #declaring a variable 'docid' to get the 'data-docid' of 'cardrationale'
    print(docid)   #to print the value in the variable 'docid' viz the 'data-docid' attribute of 'cardrationale'
    sql="INSERT INTO docid (docid) VALUES ('%s')" %(docid)   #declaring a variable 'sql' and writing a query which will insert the value of the 'docid' variable, in the column 'docid' of the table 'docid'
    a.execute(sql)   #using the execute() of the cursor object to execute the query specified in the 'sql' variable
    conn.commit()   #as the program completed executing the query, calling the commit() to commit the changes to the database
    print()   #to print a blank line