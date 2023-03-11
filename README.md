# PYTHON Projects

Collection of my python scripts from newest to oldest

### ycombinator news scraper

Sorts the news section on ycombinator from highest to lowest scores instead of using its algorithm for easy reading

### Flight Deal Finder (100 days 39-40)

Communicates with a [Strapi](https://strapi.io/) instance that I installed on an ubuntu VM. This program connect with Strapi to collect the locations of places you would like to visit and how much you will be willing for looking to spend on a flight. It will then connect to Kiwi's Tequila API to check and see if there are flights available for lower than your set price. If there are the program can be setup to either email or SMS you. Unfortunately most email and SMS software costs money now, so for now it just prints a message. I have setup SMTP servers on my home PC but they are unable to send emails outside of the network.

TODO - Work on UI - Create user inputs and then user creation

### Sheety/OpenAI Workout Tracker (100 days 38)

Uses Nutritionx to generate a json response with a user inputted sentence (EG: "I went for a walk for 2 kilometers it took 15 minutes"), then uses nutritionx openAI connection to calculate calories burned. With this json information it updates your sheety connected google sheet for easy tracking.

### Yoga Tracker (100 days 37)

Simple script that needs to be polished. Using Pixe.la API and json to post and put and create graphs to track habits.

### Stock Trader News Alert (100 days 36)

Uses alphavantage and newsapi.org APIs to check a stock. Calculates if stock has fallen or risen more than 5% between two closes then can be setup to send you a SMS or email with 3 of the latest relevant news stories to the stock ticker.

### Weather it will rain/snow (100 days 35)

Program checks openweather API then checks if the weather ID is less then 800 for the next 24 hours it will fire off an SMS alerting you the fact.

### Quizzler (100 days 34)

Upgraded the old quiz CLI to a tkinter quiz app that uses API requests to get a series of questions.

### ISS Tracker and EMAILer (100 days 33)

Every 60 seconds this program tracks the ISS using their API, also tracks sunset/sunrise using supplied latitude/longitude. Performs distance calculation from the ISS, will send out an email telling you to check outside when the ISS is closer than 5 degrees lat/long, and the sun is down.

### Kanye Says Actual Motivation Things 

Uses tkinter, request, and random, to read motivation quote API so Kanye says actually useful things rather than whatever he is going on about.

###  Birthday Reminder  (100 days 32) 

This program is using Pandas, smtplib, os, datetime, to access a supplied list of people and dates, and if hosted online (via pythonanywhere) you can use this python program to have it send you an email if someones birthday comes up today.

###  Monday Motivational Emailer (100 days 32)

Picks a random motivational quote from a supplied .csv then emails this to you using your configured SMTP. If hosted online this will email you every Monday.

### Flashcard Project (100 days 31 capstone project) 

Flashcard project that will take ANY language that is compatible with google translate (you can create a flashcard list via google sheets using =GOOGLETRANSLATE()) and create flashcards. This will go through the list of flashcards and then create a list of words you need to work on depending on the users answer.

### New Lastpass 2.0 (100 days 30) 

Password manager 2.0. Detects if JSON file exists and if it doesn't creates it. Can also search for previously generated passwords that have been saved to the JSON file.

###  New Lastpass (100 days 29) 

Password Manager GUI. Generates a secure password, and saves that information along with the website and username to a datafile stored locally.

###  Pomodore app (100 days 28) 

Breaks down work sessions into the pomodoro technique to allow better learning or better workflow. Tracks the number of work sessions and breaks.

###  Kilometers to miles converter in tkinter (100 days 27) 

Uses args and kwargs to convert.

###  NATO Phonetic Name Translator (100 days 26) 

Goes through a pandas dataframe containing NATO phonetic names, and using list comprehension cycles through the name given and outputs the NATO phonetics for any given name.

###  US States Game (100 days 25)

Guess the correct states in the USA. This uses pandas datafram to parse through the list of states then outputs a textfile for the states you have missed.

###  Mail Maker (100 days day 24) 

Takes a custom letter file and a name list file and combines them to create custom mail messages.

###  Snake with highscores (100 days day 24) 

Snake game but reads and writes to a datafile that contains high scores.

###  Frogger but Turtle (100 days day 23) 

Frogger game with turtle module

###  Pong (100 Days 22) 

I made pong. It's a 50 year old game and it was hard.

###  Snake Game (100 days 21) 

Snake game with turtle module

###  Turtle Racer (100 days day 19) 

Creates 6 turtles, bet on a turtle, see if your turtle is the winner. Uses OOP to assign 6 turtles different specified colors then while playing assigned each turtle random speeds while playing. End's when a turtle reaches specific coordinate.

###  Damien Hurst Dots (100 days 18) 

A program thaat will generate a window full of dots for the specified amount of dots and size. 

###  Random Walk (100 days 18) 

random walk in turtle

###  Quiz program (100 days 17) 

OOP quiz program that can take many forms of question data and run a quiz against it.

###  Coffee machine v2.0 (100 days 16) 

same function as before but using OOP to clean up code and improve functionality

###  Coffee machine (100 days 15) 

a coffee machine that compares the resouces it has available with different menu options and then takes payment to make a drink if the resources are available. also has a report function to display available resources and can turn off for maintenance.

###  Higher or lower game (100 days 14) 

guess if the instagram account has higher or lower followers than another

###  number guesser (100 days 12) 

guess a number between 1 and 100 in different definied rounds

###  blackjack (100 days 11) 

blackjack

###  calculator (100 days 10) 

calculator (simple)

###  silent auction program (100 days 9)

caesar cipher encoder and decoder (100 days 8)

###  hangman game (100 days 7)

###  passwordgenerator.py 

Creates a random password from specified lengths (100 days)

###  highestscore.py 

picks the highest score from a list (100 days)

###  fizzbuzz.py 

fizzbuzz game (100 days)

###  averageheight.py 

calculates average height (100 days)

###  addingevens.py 

adds all even numbers in a series of numbers

###  0xparse.py 

A program that crawls a website and extracts all the links from the website.

###  txt2pdf.py 

A program that converts a text file into a PDF.

###  ShowCollection.py 

A program that keeps a list of your favorite movies and TV shows, and allows you to add, remove, and search for items in the list.

###  rockpaperscissors.py 

A program that plays a simple game of rock-paper-scissors against the computer.

###  temperature_converter.py 

A program that converts temperatures from Fahrenheit to Celsius and vice versa.

###  madlib.py 

A program that generates a mad-libs story with user input.
