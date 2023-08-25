from helpers import user_exists, get_user, saving_userdetails_db,displaying_user,updating_userdetails,deleting_user
from helpers import trip_exists, displaying_trips,get_trip,saving_tripdetails_db,get_user_id,updating_tripdetails,deleting_trip
from helpers import expense_exists, displaying_expenses,get_trip_id,get_expense,saving_expensedetails,get_expense_id,updating_expensedetails,deleting_expense
from header import welcome
from helpers import calculating_trip_cost,calculate_total_expenses

def main():
    
    welcome()
    print("Welcome to Travel expense calculating app!!")
    user_name = input("Enter user name, checking if user exists already ")  #adding user CRUD
    if user_exists(user_name):
        print(f"User already exists ")
        displaying_user(user_name)
    else:
        print("User do not exist. add user details")
        user_name,mail_id,phone_no = get_user()
        saving_userdetails_db(user_name,mail_id,phone_no)
        print("user saved")
        displaying_user(user_name)
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
            print("Going back to main menu")
            break
    while True:
        delete = input("Do you want to delete User details? (yes/no)").lower()
        if delete == 'yes':
            deleting_user(user_name)
            print("User deleted from database going back to main menu")
            break
        elif delete == 'no':
            print("Back to main menu")
            break
    user_name = input("Enter user Name associated with the trip: ")   #adding Trips CRUD
    print("Checking if trip details exists already: ")
    if trip_exists(user_name):
        print(f"Trips already exists associated with {user_name} in database. ")
        displaying_trips(user_name)
        add = input("Do you want to add more trips? (yes/no)").lower()
        if add == 'yes':
            start_place,end_place,avg_gas_price,fuel_efficiency_mpg = get_trip()
            user_id = get_user_id(user_name)
            saving_tripdetails_db(start_place,end_place,avg_gas_price,fuel_efficiency_mpg,user_id)
            print("trip details saved")
        elif add == 'no':
            print("going back to main menu")
    else:
        print("No trips exist with this user. add new trip details")
        start_place,end_place,avg_gas_price,fuel_efficiency_mpg = get_trip()
        user_id = get_user_id(user_name)
        saving_tripdetails_db(start_place,end_place,avg_gas_price,fuel_efficiency_mpg,user_id)
        print("trip details saved")
        displaying_trips(user_name)
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
            print("Going back to main menu")
            break
    while True:
        delete = input("Do you want to delete Trip details? (yes/no)").lower()
        if delete == 'yes':
            startplace = input("Enter start place for trip to delete: ")
            endplace = input("Enter end place for trip to delete: ")
            deleting_trip(user_name, startplace, endplace)
            print("Trip deleted from database going back to main menu")
            break
        elif delete == 'no':
            print("Back to main menu")
            break

    user_name = input("Enter user Name associated with the expense: ")   #adding Expenses CRUD
    print("Checking if expense details exists already: ")
    if expense_exists(user_name):
        print(f"Expenses already exists associated with {user_name} in database. ")
        displaying_expenses(user_name)
        while True:
            add = input("Do you want to add more expenses? (yes/no)").lower()
            if add == 'yes':
                trip_id = get_trip_id(user_name)
                trip_id = int(input("Enter trip_id to add "))
                expense_type,spent_amount = get_expense()
                #trip_id = get_trip_id(user_name)
                saving_expensedetails(expense_type,spent_amount,trip_id)
                print("expense details saved")
                displaying_expenses(user_name)
                break
            elif add == 'no':
                print("going back to main menu")
                break
    else:
        print("no expense details found for this user")
        expense_type,spent_amount = get_expense()
        trip_id = get_trip_id(user_name)
        saving_expensedetails(expense_type,spent_amount,trip_id)
        print("expense details saved")
        displaying_expenses(user_name)

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
            print("Going back to main menu")
            break
    
    while True:
        delete = input("Do you want to delete Expense details? (yes/no)").lower()
        if delete == 'yes':
            expense_id = get_expense_id(user_name)
            expense_id = input("Enter expense id to delete: ")
            deleting_expense(expense_id)
            print("Expense deleted from database going back to main menu")
            break
        elif delete == 'no':
            print("Back to main menu")
            break
    print("Calculating trip expense for username")
    user_name =input("Enter username to display trip details: ")
    displaying_trips(user_name)
    #tripid = input("Enter tripid associated with user to calculate distance: ")
    print("Calculating total distance of trip: ")
    calculating_trip_cost(user_name)
    print("Calculating total expenses cost for entire trip")
    calculate_total_expenses(user_name)

if __name__=="__main__":        
    main()