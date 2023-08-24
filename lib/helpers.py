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

#CRUD operation on User details
def get_user():
    user_name = input("Enter user name: ")
    mail_id = input("Enter email: ")
    phone_no = input("Enter phone number: ")
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
            print(f"User details updated: {updating_user}")
            return updating_user
    else:
        print("user not found")
def deleting_user(user_name):
    deleting_user = session.query(User).filter_by(user_name = user_name).first()
    if deleting_user:
        session.delete(deleting_user)
        session.commit()
        print(f"user deleted: {deleting_user}")
    else:
        print("user not found")
def displaying_user(user_name):
    displaying_user = session.query(User).filter_by(user_name = user_name).first()
    if displaying_user:
        #session.display(displaying_user)
        print("User details: ")
        print(f"User id: {displaying_user.user_id}")
        print(f"User name: {displaying_user.user_name}")
        print(f"User email: {displaying_user.mail_id}")
        print(f"User phone: {displaying_user.phone_no}")
        print(f"User created at: {displaying_user.created_at}")
    else:
        print("User not found")

#CRUD operation on Trips details with associated User
def trip_exists(user_id):
    trips = session.query(Trip).filter_by(user_id=6).all()
    return trips

def trip_exists(user_name):
    trips = session.query(Trip).join(User).filter(User.user_name == user_name).all()
    for trip in trips:
        #print(trip)
        return trip
    #print(trips)
    #return trips

def displaying_trips(user_name):
    displaying_trips = session.query(Trip).join(User).filter(User.user_name==user_name).all()
    for trip in displaying_trips:
        #print(trip)
        if trip:
        #session.display(displaying_user)
            print("Trip details: ")
            print(f"Trip id: {trip.trip_id}")
            print(f"Start Place: {trip.start_place}")
            print(f"Destination place: {trip.end_place}")
            print(f"gas price: {trip.avg_gas_price}")
            print(f"Fuel efficiency: {trip.fuel_efficiency_mpg}")
            print(f"User id: {trip.user_id}")
        else:
            print("User not found")

def get_trip():
    start_place = input("Enter start place: ")
    end_place = input("Enter destination place: ")
    avg_gas_price = float(input("Enter gas cost: "))
    fuel_efficiency_mpg = float(input("Enter miles per gallon: "))
    return start_place,end_place,avg_gas_price,fuel_efficiency_mpg
def saving_tripdetails_db(start_place,end_place,avg_gas_price,fuel_efficiency_mpg,user_id):
    new_trip = Trip(
        start_place = start_place,
        end_place = end_place,
        avg_gas_price = avg_gas_price,
        fuel_efficiency_mpg =fuel_efficiency_mpg,
        user_id = user_id
    )
    session.add(new_trip)
    session.commit()
def get_user_id(user_name):
    user = session.query(User).filter(User.user_name == user_name).first()
    if user:
        return user.user_id
    else:
        return None
def updating_tripdetails(user_name,update_type,update_value):
    updating_trips = session.query(Trip).join(User).filter(User.user_name==user_name).all()
    for trip in updating_trips:
        #print(trip)
        if trip:
            if update_type == "startplace":
                trip.start_place = update_value
            elif update_type == "endplace":
                trip.end_place = update_value
            elif update_type == "gascost":
                trip.avg_gas_price = float(update_value)
            elif update_type == "mpg":
                trip.fuel_efficiency_mpg = int(update_value)
            session.commit()
            print(f"trip details updated: {trip} ")
            return trip
        else:
            print("Trip not found")
def deleting_trip(user_name,startplace,endplace):
    deltrip = session.query(Trip).join(User).filter(User.user_name==user_name, Trip.start_place == startplace, Trip.end_place == endplace).first()
    if deltrip:
        session.delete(deltrip)
        session.commit()
        print(f"trip deleted: {deltrip}")
    else:
        print("trip not found")

