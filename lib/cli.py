from helpers import user_exists, get_user, saving_userdetails_db
from header import welcome

def main():
    
    welcome()
    print("Welcome to Travel expense calculating app!!")
    user_name = input("Enter user name, checking if it exists already ")
    if user_exists(user_name):
        print(f"User already exists ")
    else:
        print("User do not exist. add user details")
        user_name,mail_id,phone_no = get_user()
        saving_userdetails_db(user_name,mail_id,phone_no)
        print("user saved")

        
main()