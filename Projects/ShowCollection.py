# Show Collection by 0xskar
#
# A program that keeps a list of your favorite movies and TV shows, and allows you to add, remove, and search for items in the list.
# 

import mysql.connector

connection = mysql.connector.connect(user='0xskar',
                                     password='passw0rd',
                                     host='192.168.0.34',
                                     database='ShowCollection')

def MAIN_MENU_SELECT(): 
    input_pass = 0
    while(input_pass == 0):
        try:
            global menu_select
            menu_select = int(input("Please, select a option: "))
            if menu_select <= menu_choices[-1] and menu_select >= menu_choices[0]:
                break
            else:
                print("Not a valid menu option.")
        except ValueError:
            print("Not a valid menu option.")
        
def LIST_MOVIES():        
    cursor = connection.cursor()
    query = 'SELECT * FROM movies'
    rows = cursor.fetchall()
    print("***************************************************")
    print("                    LIST MOVIES                    ")
    print("***************************************************")
    for row in rows:
        print(row)
    cursor.close()
    input_pass = 0
    MAIN_MENU_SELECT()
    
def ADD_MOVIES():
    print("***************************************************")
    print("                    ADD MOVIES                     ")
    print("***************************************************")
    input_pass = 0
    MAIN_MENU_SELECT()


while connection.is_connected():
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

    print(menu_select)

    while int(menu_select) == 1:
        LIST_MOVIES()
    while int(menu_select) == 2:
        print("LIST TV SHOWS")
        input_pass = 0
        MAIN_MENU_SELECT()
    while int(menu_select) == 3:
        print("SEARCH DATABASE")
        input_pass = 0
        MAIN_MENU_SELECT()
    while int(menu_select) == 4:
        ADD_MOVIES()
    while int(menu_select) == 5:
        print("Add a TV SHOW")
        input_pass = 0
        MAIN_MENU_SELECT()
    while int(menu_select) == 6:
        print("Delete Movie")
        input_pass = 0
        MAIN_MENU_SELECT()
    while int(menu_select) == 7:
        print("Delete TV Show")
        input_pass = 0
        MAIN_MENU_SELECT()
    

    connection.close()
    print("Disconnected.")
else:
    print("Couldn't connect to a Database.")
connection.close()