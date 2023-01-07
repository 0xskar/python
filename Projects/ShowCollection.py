# Show Collection by 0xskar
#
# A program that keeps a list of your favorite movies and TV shows, and allows you to add, remove, and search for items in the list.
# 

import mysql.connector
connection = mysql.connector.connect(user='0xskar',
                                     password='passw0rd',
                                     host='192.168.0.34',
                                     database='ShowCollection')
if connection.is_connected():
    print("             SHOW COLLECTION by 0xskar             ")
    print("***************************************************")
    print("                     MAIN MENU                     ")
    print("***************************************************")
    print("1) List Movies           ")
    print("2) List TV Shows         ")
    print("3) Search Database       ")
    print("4) Add a Movie           ")
    print("5) Add a TV Show         ")
    print("6) Delete a Movie        ")
    print("7) Delete a TV Show      ")
    print("***************************************************")
    menu_options = [i for i in range(1, 7)]
    menu_select = input("Please, select a option: ")
    while(int(menu_select) not in menu_options):
        print("Not a valid menu option.")
        menu_select = input("Please, select a option: ")
            





    connection.close()
    print("Disconnected.")
else:
    print("Couldn't connect to a Database.")
connection.close()