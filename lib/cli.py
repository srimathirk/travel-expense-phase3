from helpers import  user_exists,get_user, saving_userdetails_db,displaying_user,updating_userdetails,deleting_user
from helpers import trip_exists, displaying_trips,get_trip,saving_tripdetails_db,get_user_id,updating_tripdetails,deleting_trip
from helpers import expense_exists, displaying_expenses,get_trip_id,get_expense,saving_expensedetails,get_expense_id,updating_expensedetails,deleting_expense
from header import welcome
from helpers import calculate_total_expenses,adding_expenses,adding_more_expense,clear_screen
import time
from simple_term_menu import TerminalMenu
from prettycli import red, blue, yellow, color
#from db.models import User
def main():
    
    welcome()
    print("Welcome to Travel expense calculating app!!")
    clear_screen(1)
    user_name = input("Enter user name, checking if user exists already: ")  #adding user CRUD
    if user_exists(user_name):
        print(f"User already exists!!")
        displaying_user(user_name)
        clear_screen(1)
    else:
        print("User do not exist. add user details")
        user_name,mail_id,phone_no = get_user()
        saving_userdetails_db(user_name,mail_id,phone_no)
        print("user saved")
        displaying_user(user_name)
        clear_screen(1)
    # print("Options: update, delete")
    # option = input("Choose an option: ").lower()
    user_options = ["update","delete","continue to userTrips details"]
    user_terminal_menu = TerminalMenu(user_options)
    user_entry_index = user_terminal_menu.show()
    print(f"You selected {user_options[user_entry_index]}!")
    selected_user_option = user_options[user_entry_index]
    if selected_user_option == "update":
        while True:
            update = input("Do you want to update User details? (yes/no)").lower()
            if update == 'yes':
                update_type = input("Do you want to update (mail/phone): ").lower()
                if update_type in ["mail","phone"]:
                    update_value = input(f"Enter new {update_type}: ")
                    updating_userdetails(user_name,update_type,update_value)
                else:
                    print("Invalid option")
            elif update == 'no':
                print("you selected no update")
                break
    elif selected_user_option == "delete":
        while True:
            delete = input("Do you want to delete User details? (yes/no)").lower()
            if delete == 'yes':
                deleting_user(user_name)
                print("User deleted from database going back to main menu")
                break
            elif delete == 'no':
                print("you selected no delete")
                break
    elif selected_user_option == "continue to userTripsdetails":
        print(f"Showing trip details for {user_name}")
    time.sleep(1)
    #user_name = input("Enter user Name associated with the trip: ")   #adding Trips CRUD
    print(f"Checking if trip details exists already: ")
    if trip_exists(user_name):
        print(f"Trips already exists with {user_name} in database !!")
        clear_screen(1)
        displaying_trips(user_name)
        clear_screen(1)
        add = input("Do you want to add more trips? (yes/no)").lower()
        if add == 'yes':
            start_place,end_place,avg_gas_price,fuel_efficiency_mpg = get_trip()
            user_id = get_user_id(user_name)
            saving_tripdetails_db(start_place,end_place,avg_gas_price,fuel_efficiency_mpg,user_id)
            print("trip details saved")
        elif add == 'no':
            print("you selected no adding extra trips")
            clear_screen(1)
    else:
        print("No trips exist with this user. add new trip details")
        clear_screen(1)
        start_place,end_place,avg_gas_price,fuel_efficiency_mpg = get_trip()
        user_id = get_user_id(user_name)
        saving_tripdetails_db(start_place,end_place,avg_gas_price,fuel_efficiency_mpg,user_id)
        print("trip details saved")
        displaying_trips(user_name)
        # clear_screen(2)
    trip_options = ["update","delete","continue to expenses"]
    trip_menu = TerminalMenu(trip_options)
    trip_entry_index = trip_menu.show()
    print(f"You selected {trip_options[trip_entry_index]}!")
    selected_trip_option = trip_options[trip_entry_index]
    if selected_trip_option == "update":
        while True:
            update = input("Do you want to update Trip details? (yes/no)").lower()
            trip_id = get_trip_id(user_name)
            #trip_id = int(input("Enter trip_id to update"))
            if update == 'yes':
                trip_id = int(input("Enter trip_id to update: "))
                update_type = input("Do you want to update (startplace/endplace/gascost/mpg): ").lower()
                if update_type in ["startplace","endplace","gascost","mpg"]:
                    update_value = input(f"Enter new {update_type}: ")
                    updating_tripdetails(trip_id,update_type,update_value)
                else:
                    print("Invalid option")
            elif update == 'no':
                print("you selected no update")
                break
    elif selected_trip_option == "delete":
        while True:
            delete = input("Do you want to delete Trip details? (yes/no)").lower()
            if delete == 'yes':
                startplace = input("Enter start place for trip to delete: ")
                endplace = input("Enter end place for trip to delete: ")
                deleting_trip(user_name, startplace, endplace)
                print("Trip deleted from database going back to main menu")
                break
            elif delete == 'no':
                print("you selected no delete")
                break
    elif selected_trip_option == "continue to expenses":
        print(f"showing expense details associated with a Trip for {user_name}")
    clear_screen(1)
    time.sleep(2)
    #user_name = input("Enter user Name associated with the expense: ")   #adding Expenses CRUD
    print(f"Checking if expense details exists already: ")
    if expense_exists(user_name):
        print(f"Expenses already exists associated with {user_name} in database. ")
        clear_screen(1)
        displaying_expenses(user_name)
        clear_screen(1)
        adding_more_expense(user_name)
    else:
        print("no expense details found for this user")
        adding_expenses(user_name)
        #add = input("Do you want to add more expenses? (yes/no)").lower()
        clear_screen(1)
        adding_more_expense(user_name)
    expense_options = ["update","delete","continue to calculate total expenses"]
    expense_menu = TerminalMenu(expense_options)
    expense_entry_index = expense_menu.show()
    print(f"You selected {expense_options[expense_entry_index]}!")
    selected_expense_option = expense_options[expense_entry_index]
    if selected_expense_option == "update":
        while True:
            update = input("Do you want to update Expense details? (yes/no)").lower()
            expense_id = get_expense_id(user_name)
            #trip_id = int(input("Enter trip_id to update"))
            if update == 'yes':
                trip_id = int(input("Enter trip_id to update: "))
                expense_id = int(input("Enter expense_id to update: "))
                update_type = input("Do you want to update (category/amount): ").lower()
                if update_type in ["category","amount"]:
                    update_value = input(f"Enter new {update_type}: ")
                    updating_expensedetails(expense_id,update_type,update_value)
                else:
                    print("Invalid option")
            elif update == 'no':
                print("you selected no update")
                break
    elif selected_expense_option == "delete":
        while True:
            delete = input("Do you want to delete Expense details? (yes/no)").lower()
            if delete == 'yes':
                expense_id = get_expense_id(user_name)
                expense_id = input("Enter expense id to delete: ")
                deleting_expense(expense_id)
                print("Expense deleted from database going back to main menu")
                break
            elif delete == 'no':
                print("you selected no delete")
                break
    elif selected_expense_option == "continue to calculate total expenses":
        print(f"Calculating expense details for {user_name}")
    time.sleep(1)
    #print("Calculating trip expense for username")
    #user_name =input("Enter username to display trip details: ")
    #displaying_trips(user_name)
    #print("Calculating total distance of trip: ")
    #calculating_trip_cost(user_name)
    print("Calculating total expenses cost for entire trip")
    clear_screen(1)
    calculate_total_expenses(user_name)
    clear_screen(1)
    print("Thank you for using cli travel app")
if __name__=="__main__":        
    main()