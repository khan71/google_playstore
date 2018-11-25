from bs4 import BeautifulSoup   #from the bs4 package of python import BeautifulSoup library
import requests   #import the package requests which is an HTTP library to ping a website or portal for information
import pymysql   #import PyMySQL which is a pure-Python MySQL client library

conn=pymysql.connect(host='127.0.0.1',port=3307,user='root',password='8793',db='task2nd')   #declaring a variable 'conn' which used to eastablish the connection with mysql using the arguments user(username) and password to authenticate, db for the database name to use when connecting with the MySQL server, the host name of the MySQL server and the TCP/IP port of the MySQL server which must be an integer.
a=conn.cursor()   #creating a cursor object as it allows python to execute sql commands in database session. declaring a variable 'a' that will execute conn.cursor()

source=requests.get('https://medium.mybridge.co/38-amazing-android-open-source-apps-java-1a62b7034c40').text   #declaring a variable 'source' to get the source code of the website using the requests library (requests.get() returns a response object). (.text at the end is used to get the source code from the response object). 

soup=BeautifulSoup(source,'lxml')   #declaring a variable 'soup' which is used to pass the html file to the BeautifulSoup library along with the parser. 'lxml' is the parser

atags=soup.find_all('a',class_='markup--anchor markup--h4-anchor')   #declaring a variable 'atags' to get the information from the tags. using find() we can pass in arguments of attributes and is used to find the exact tag that we are looking for. find_all() returns the list of all the tags that matchesthese arguments. (find_all() to search for all the tags 'a' with the class='markup--anchor markup--h4-anchor')
#x=len(atags)
#print(x)
print('1st for loop for rank')   #to print('1st for loop for rank')
for atag in atags:   #for loop to loop through the list that the variable 'atags' returns 
    rank=atag.text   #declaring a variable 'rank' to get the text attribute of the tag 'atag'
    print(rank)   #to print the value in the variable 'rank' viz the text attribute of the 'atag'
    sql="INSERT INTO application_rank (rank_id) VALUES ('%s')" %(rank)   #declaring a variable 'sql' and writing a query which will insert the value of the 'rank' variable, in the column 'rank_id' of the table 'application_rank'
    a.execute(sql)   #using the execute() of the cursor object to execute the query specified in the 'sql' variable
    conn.commit()   #as the program completed executing the query, calling the commit() to commit the changes to the database
    print()   #to print a blank line

print('2nd for loop for url')   #to print('2nd for loop for url')
#x=len(atags)
#print(x)
for atag in atags:   #for loop to loop through the list that the variable 'atags' returns 
    url=atag.get('href')   #.get() returns a value for the specified/given key. declaring a variable 'url' that gets the 'href' attribute of the tag 'atag'
    print(url)   #to print the value in the variable 'url' viz the 'href' attribute of the 'atag'
    sql="INSERT INTO url (href) VALUES ('%s')" %(url)   #declaring a variable 'sql' and writing a query which will insert the value of the 'url' variable, in the column 'href' of the table 'url'
    a.execute(sql)   #using the execute() of the cursor object to execute the query specified in the 'sql' variable
    conn.commit()   #as the program completed executing the query, calling the commit() to commit the changes to the database
    print()   #to print a blank line

ptags=soup.find_all('p',class_='graf graf--p graf-after--h4')   #declaring a variable 'ptags' to get the information from the tags. using find() we can pass in arguments of attributes and is used to find the exact tag that we are looking for. find_all() returns the list of all the tags that matchesthese arguments. (find_all() to search for all the tags 'p' with the class='graf graf--p graf-after--h4')
print('3rd for loop for application name')   #to print('3rd for loop for application name')
#x=len(ptags)
#print(x)
for ptag in ptags:   #for loop to loop through the list that the variable 'ptags' returns 
    name=ptag.text   #declaring a variable 'name' to get the text attribute of the tag 'ptag'
    toprint=name.partition("[")[0]   #declaring a variable 'toprint' which will store the text attribute of the tag 'ptag' until a '[' occurs
    print(toprint)   #to print the value in the variable 'toprint' viz the text attribute of the 'ptag'
    sql="INSERT INTO application_name (appname) VALUES ('%s')" %(toprint)   #declaring a variable 'sql' and writing a query which will insert the value of the 'toprint' variable, in the column 'appname' of the table 'application_name'
    a.execute(sql)   #using the execute() of the cursor object to execute the query specified in the 'sql' variable
    conn.commit()   #as the program completed executing the query, calling the commit() to commit the changes to the database  
    print()   #to print a blank line

print('4th loop for application id')   #to print('4th for loop for application id')
#x=len(ptags)
#print(x)
for ptag in ptags:   #for loop to loop through the list that the variable 'ptags' returns 
    id=ptag.get('id')   #.get() returns a value for the specified/given key. declaring a variable 'id' that gets the 'id' attribute of the tag 'ptag'
    print(id)   #to print the value in the variable 'id' viz the 'id' attribute of the 'ptag'
    sql="INSERT INTO doc_id (appid) VALUES ('%s')" %(id)   #declaring a variable 'sql' and writing a query which will insert the value of the 'id' variable, in the column 'appid' of the table 'doc_id'
    a.execute(sql)   #using the execute() of the cursor object to execute the query specified in the 'sql' variable
    conn.commit()   #as the program completed executing the query, calling the commit() to commit the changes to the database      
    print()   #to print a blank line