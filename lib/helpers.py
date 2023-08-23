from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from db.models import User, Trip, Expense #importing class from models.py

#connecting database engine and setting up session
engine= create_engine("sqlite:///db/travel_records.db")
Session = sessionmaker(bind=engine)
session = Session()

def get_user():
    user_name = input("Enter user name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    return user_name, mail_id,phone_no
def user_exists(user_name):
    user = session.query(User).filter_by(user_name = user_name).first()
    return user
def saving_userdetails_db(name,email,phone):
    new_user = User(
        user_name = name,
        mail_id =email,
        phone_no = phone,
        created_at = datetime.now()
    )
    session.add(new_user)
    session.commit()
def updating_userdetails(user_name,update_type,update_value):
    updating_user = session.query(User).filter_by(user_name = user_name).first()
    if updating_user:
        if update_type == "mail_id":
            updating_user.mail_id = update_value
        elif update_type == "phone_no":
            updating_user.phone_no = update_value
            session.commit()
            print("User details updated" updating_user)
            return updating_user
    else:
        print("user not found")
def deleting_user(user_name):
    deleting_user = session.query(User).filter_by(user_name = user_name).first()
    if deleting_user:
        session.delete(deleting_user)
        session.commit()
        print("user deleted" deleting_user)
    else:
        print("user not found")
def displaying_user(user_name):
    displaying_user = session.query(User).filter_by(user_name = user_name).first()
    if displaying_user:
        #session.display(displaying_user)
        print("User details: ")
        print(f"User id: {User.user_id}")
        print(f"User name: {User.user_name}")
        print(f"User email: {User.mail_id}")
        print(f"User phone: {User.phone_no}")
        print(f"User created at: {User.created_at}")
    else:
        print("User not found")
