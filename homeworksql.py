
import mysql.connector #import connector
from mysql.connector import Error

#create connection
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occured")

    return connection

connection = create_connection("cis3368.c8kqueubd72o.us-east-1.rds.amazonaws.com", "antho305", "Antho2ss", "cis3368db")#created connection for data base

        





#menu for outputs
def menu():
    print("a - Add contact")
    print("d - Remove contact")
    print("u - Update contact details")
    print("b - Output all contacts in alphabetical order")
    print("c - Output all contacts by creation date")
    print("o - Output all contacts")
    print("q - Quit")

menu()
option = str(input("Choose your option: "))
#allows for options to function
while option != 'q':
    if option == 'a':
        print("Add contact")
        try:#runs option
            ID = input("ID: ")
            contactDetails = input("Contact name: ")
            creationDate = input("Date: ")
            
            #sql command for insertion
            mycursor = connection.cursor()
            sql = """INSERT INTO contacts 
            (ID, contactDetails, creationDate)
            VALUES('{}','{}','{}')""".format(ID,contactDetails,creationDate)

            mycursor.execute(sql)
            connection.commit()
            mycursor.close()

        except Error as E:
            print(f"An error '{E}' has occured ")
        #Removes contacts

    elif option == 'd':
        print("Remove Contact")
        try:
            contactDetails = input("Contact name: ")
            mycursor = connection.cursor()
            sql = "DELETE FROM contacts WHERE contactDetails = '{}' ".format(contactDetails)

            mycursor.execute(sql)
            connection.commit()
            mycursor.close()
        except Error as E:
            print(f"An error '{E}' has occured ")





#Updates contact details
    elif option == 'u':
        try:
            print("Update contact details")#message to print
            contactDetails = input("Contact Name: ")
            updatedContact = input("Updated Contact Name: ")
            mycursor = connection.cursor()
            sql = "UPDATE contacts SET contactDetails = '{}' WHERE contactDetails = '{}' ".format(updatedContact, contactDetails)#sql syntax to update contact details
            mycursor.execute(sql)

            connection.commit()#commits the connection
            mycursor.close()
        except Error as E:
            print(f"An error '{E}' has occured ")#prints message 


#outputs contacts in alphabetical order
    elif option == 'b':
        print("Output all contacts in alphabetical order")
        mycursor = connection.cursor()
        sql = "SELECT * FROM contacts ORDER BY contactDetails"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)



#outputs contacts by creation
    elif option == 'c':
        print("Output all contacts by creation date")
        mycursor = connection.cursor()
        sql = "SELECT creationDate FROM contacts"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

        
#outputs all contacts
    elif option == 'o':
        print(" Output all contacts")
        mycursor = connection.cursor()
        mycursor.execute("SELECT contactDetails FROM contacts")#action to pull from contactDetails
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
   #break code 
    else:
        break
    menu()
    option = str(input("Choose your option: "))