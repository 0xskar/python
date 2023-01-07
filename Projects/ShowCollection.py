# Show Collection by 0xskar
#
# A program that keeps a list of your favorite movies and TV shows, and allows you to add, remove, and search for items in the list.
# 

import mysql.connector
connection = mysql.connector.connect(user='0xskar',
                                     password='passw0rd',
                                     host='192.168.0.34',
                                     database='ShowCollection')



# check options
def MAIN_MENU_SELECT(): 
    input_pass = 0
    while(input_pass == 0):
        try:
            menu_select = int(input("Please, select a option: "))
            if menu_select <= menu_choices[-1]:
                break
            else:
                print("Not a valid menu option.")
        except ValueError:
            print("Not a valid menu option.")
        

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

    # list of integers as string
    menu_options = [i for i in range(1, 8)]
    # empty list to store integers
    menu_choices = []
    # convert options string to integers
    for x in menu_options:
        menu_choices.append(int(x))

    print(menu_choices)

    MAIN_MENU_SELECT()

    connection.close()
    print("Disconnected.")
else:
    print("Couldn't connect to a Database.")
connection.close()