# Show Collection by 0xskar
#
# A program that keeps a list of your favorite movies and TV shows, and allows you to add, remove, and search for items in the list.
# 

import mysql.connector

connection = mysql.connector.connect(user='0xskar',
                                     password='passw0rd',
                                     host='192.168.0.34',
                                     database='ShowCollection')

def MAIN_MENU():
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

def MAIN_MENU_SELECT(): 
    global input_pass
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
    global input_pass
    cursor = connection.cursor()
    query = 'SELECT * FROM movies'
    cursor.execute(query)
    rows = cursor.fetchall()
    print("***************************************************")
    print("                    LIST MOVIES                    ")
    print("***************************************************")
    for row in rows:
        print(row)
    cursor.close()
    MAIN_MENU()
    input_pass = 0
    MAIN_MENU_SELECT()

def LIST_SHOWS():        
    global input_pass
    cursor = connection.cursor()
    query = 'SELECT * FROM tv_shows'
    cursor.execute(query)
    rows = cursor.fetchall()
    print("***************************************************")
    print("                    LIST SHOWS                    ")
    print("***************************************************")
    for row in rows:
        print(row)
    cursor.close()
    MAIN_MENU()
    MAIN_MENU_SELECT()    

def SEARCH_DB():        
    global input_pass
    cursor = connection.cursor()
    query = 'SELECT * FROM tv_shows'
    cursor.execute(query)
    rows = cursor.fetchall()
    print("***************************************************")
    print("                    SEARCH DATABASE                ")
    print("***************************************************")
    for row in rows:
        print(row)
    cursor.close()
    MAIN_MENU()
    input_pass = 0
    MAIN_MENU_SELECT()    
    
def ADD_MOVIES():
    global input_pass
    cursor = connection.cursor()    
    print("***************************************************")
    print("                    ADD MOVIES                     ")
    print("***************************************************")
    print("")
    movie_name = input("Enter the name of the movie: ")
    movie_genre = input("Enter the genre of the movie: ")
    movie_year = int(input("Enter the release year of the movie (ex: 1986): "))
    movie_rating = int(input("Rate the movie 1 out of 10: "))
    query = "INSERT INTO movies (name, genre, release_year, rating) VALUES (%s, %s, %s, %s)"
    values = (movie_name, movie_genre, movie_year, movie_rating)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    print("***************************************************")
    print("ADDED MOVIE TO DATABASE")
    print("Name:" + movie_name)
    print("Genre:" + movie_genre)
    print("Year:",movie_year)
    print("Rating:",movie_rating)
    MAIN_MENU()
    input_pass = 0
    MAIN_MENU_SELECT()

def ADD_SHOWS():
    global input_pass
    cursor = connection.cursor()    
    print("***************************************************")
    print("                    ADD TV SHOWS                   ")
    print("***************************************************")
    print("")
    show_name = input("Enter the name of the TV Show: ")
    show_genre = input("Enter the genre of the TV Show: ")
    show_year = int(input("Enter the release year of the TV Show (ex: 1986): "))
    show_rating = int(input("Rate the TV Show 1 out of 10: "))
    query = "INSERT INTO tv_shows (name, genre, release_year, rating) VALUES (%s, %s, %s, %s)"
    values = (show_name, show_genre, show_year, show_rating)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    print("***************************************************")
    print("ADDED TV SHOW TO DATABASE")
    print("Name:" + show_name)
    print("Genre:" + show_genre)
    print("Year:",show_year)
    print("Rating:",show_rating)
    MAIN_MENU()
    input_pass = 0
    MAIN_MENU_SELECT()

def DELETE_MOVIE():
    global input_pass
    cursor = connection.cursor(buffered=True)    
    print("***************************************************")
    print("                    DELETE MOVIE                   ")
    print("***************************************************")
    print("")
    movie_ID = int(input("Enter the ID of movie: "))
    select = "SELECT * FROM movies WHERE id = %s"
    query = "DELETE FROM movies WHERE id = %s"
    cursor.execute(select, (movie_ID,))  
    row = cursor.fetchone()
    cursor.execute(query, (movie_ID,))
    connection.commit()
    cursor.close()
    print("***************************************************")
    print("DELETED MOVIE FROM DATABASE")
    print(row)
    MAIN_MENU()
    input_pass = 0
    MAIN_MENU_SELECT()

def DELETE_SHOW():
    global input_pass
    cursor = connection.cursor()    
    print("***************************************************")
    print("                  DELETE TV SHOW                   ")
    print("***************************************************")
    print("")
    show_ID = int(input("Enter the ID of TV Show: "))
    select = "SELECT * FROM tv_shows WHERE id = %s"
    query = "DELETE FROM tv_shows WHERE id = %s"
    cursor.execute(select, (show_ID,))  
    row = cursor.fetchone()
    cursor.execute(query, (show_ID,))
    connection.commit()
    cursor.close()
    print("***************************************************")
    print("DELETED TV SHOW FROM DATABASE")
    print(row)
    MAIN_MENU()
    input_pass = 0
    MAIN_MENU_SELECT()

while connection.is_connected():
    print("***************************************************")
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

    MAIN_MENU_SELECT()

    if input_pass == False:
        print("break")
        break

while connection.is_connected():
    while int(menu_select) == 1:
        LIST_MOVIES()
    while int(menu_select) == 2:
        LIST_SHOWS()
    while int(menu_select) == 3:
        SEARCH_DB()
    while int(menu_select) == 4:
        ADD_MOVIES()
    while int(menu_select) == 5:
        ADD_SHOWS()
    while int(menu_select) == 6:
        DELETE_MOVIE()
    while int(menu_select) == 7:
        DELETE_SHOW()
    
else:
    print("Couldn't connect to a Database.")
connection.close()