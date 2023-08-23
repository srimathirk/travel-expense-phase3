import helpers
import header

def main():
    
    header.welcome()
    print("Welcome to Travel expense calculating app!!")
    user_name = input("Enter user name, checking if it exists already")
    if user_exists(user_name):
        print(f"User already exists : {display_user_details(user_name)}")
        
        #option = input("Do you want to (update/delete): ").lower()

main()