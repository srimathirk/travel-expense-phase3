from helpers import user_exists, get_user, saving_userdetails_db,displaying_user,updating_userdetails,deleting_user
from header import welcome

def main():
    
    welcome()
    print("Welcome to Travel expense calculating app!!")
    user_name = input("Enter user name, checking if user exists already ")
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
            update_type = input("Do you want to update (mail_id/phone_no): ").lower()
            if update_type in ["mail_id","phone_no"]:
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
    user_name = int(input("Enter user Name associated with the trip: "))
    print("Checking if trip details exists already: ")
    if trip_exists(user_name):
        print(f"Trips already exists associated with {user_name} in database. ")
        desplaying_trips(user_name)

if __name__=="__main__":        
    main()