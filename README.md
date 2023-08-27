# Travel Expense Calculator (Phase 3)
This project is based on User going on a trips and spending expenses for each trip and calculating distance by using external library, atlast calculating total expenses spent on trip with their expenses. Here we are tracking User records, tracking user on multiple trips, and  also expenses for each trip. Atlast calculating total expenses spent by user for their trip.
## Having three models/class and their relationships: 
User, Trip and Expense

User may have many trips
User and Trip table(one to many relationship)
Trip may have many expenses
Trip and Expense table(one to many relationship)

*attached database diagram in Notes folder*

Database stored :
sqlite:///travel_records.db

### class attributes
1. User class
    - user_id
    - user_name
    - mail_id
    - phone_no
    - created_at
2. Trip class
    - trip_id
    - start_place
    - end_place
    - avg_gas_price
    - fuel_efficiency_mpg
    - user_id
3. Expense class
    - expense_id
    - trip_id
    - expense_type
    - spent_amount
    
### methods/ functions used for CLI project from Classes

# for User
user_exists:
- finding/querying User by name to check weather user exists
saving_userdetails_db:
- saving new user details to databse.
updating_userdetails
- updating user by getting their field_type and updating values
displaying_user
- displaying all details of user
deleting_user
- deleting user by filtering their name
# for Trip
Trip_exists:
- finding/querying Trip by username to check weather trip exists
saving_Tripdetails_db:
- saving new trip details to databse.
updating_Tripdetails
- updating trip by getting their field_type and updating values
displaying_trip
- displaying all details of trip
deleting_trip
- deleting trip by filtering their name
# for Expense
expense_exists:
- finding/querying expense by username to check weather expense exists
saving_expensedetails_db:
- saving new expense details to databse.
updating_expensedetails
- updating expense by getting their field_type and updating values
displaying_expense
- displaying all details of expense
deleting_expense
- deleting expense by filtering their username with respect to trip associated with userid
## From Trip
calculating_distance:
    - by taking start_pace and end_place details by using external library using *import geopy* locating the places cordinates and by using their latitudes and longitudes calculating distance.
calculate_trip_expense:
    - After calculating distance , calculating number of gallons = dividing distance (m) / fuelefficiency (mpg)
    trip cost = gallons * gas price
## from trip and expense
calculate_total_expenses:
    - User id associated for each trip in trips and trip id associated for each expense in expenses calculating total expenses by adding all the expense cost with trip expense cost that gives total expenses cost for a user. 
### external library for cli

*attached cli template in Notes folder*

for cli added external librarys
-import simple terminal-menu
 for making options in most user interactive way
- import pretty cli
 for making colors and to make commands in user lookable
 to run external librarys make sure to run pipenv shell

to execute the Cli project in Command line Interface terminal
    **run the command** 
    fork and clone the project from github link: https://github.com/srimathirk/travel-expense-phase3
    open in vscode by code .
    run pipenv shell
    open inside lib folder (cd lib) 
    *run* => python cli.py