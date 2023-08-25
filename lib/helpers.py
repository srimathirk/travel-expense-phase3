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
def updating_tripdetails(trip_id,update_type,update_value):
    trip = session.query(Trip).filter_by(trip_id=trip_id).first()
    #for trip in updating_trips:
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
def expense_exists(user_name):
    user = session.query(User).filter(User.user_name == user_name).first()
    if user:
        return session.query(Expense).join(Trip).filter(Trip.user_id == user.user_id).all()
    return False
def displaying_expenses(user_name):
    user = session.query(User).filter(User.user_name == user_name).first()
    if user:
        trips = session.query(Trip).filter(Trip.user_id == user.user_id).all()
        if trips:
            for trip in trips:
                print(f"Trip: {trip}")
                expenses = session.query(Expense).filter(Expense.trip_id == trip.trip_id).all()
                if expenses:
                    #print(f"expenses:{expenses}")
                    for expense in expenses:
                        print(f"(expense: {expense})")
                else:
                    print("no expense found")
        else:
            print("no trip found")
def get_expense():
    expense_type = input("Enter expense category: ")
    spent_amount = float(input("Enter expense amount: "))
    return expense_type, spent_amount 
def get_trip_id(user_name):
    trips = session.query(Trip).join(User).filter(Trip.user_id == User.user_id, User.user_name == user_name).all()
    for trip in trips:
        while True:
            if trip:
                return trip.trip_id
            else:
                return None
def saving_expensedetails(expense_type,spent_amount,trip_id):
    new_expense = Expense(
        expense_type = expense_type,
        spent_amount = spent_amount,
        trip_id = trip_id
    )
    session.add(new_expense)
    session.commit()
def get_expense_id(user_name):
    expenses = session.query(Expense.expense_id).join(Trip).join(User).filter(User.user_name == user_name).all()
    for expense in expenses:
        while True:
            if expense:
                return expense.expense_id
            else:
                return None

def updating_expensedetails(expense_id,update_type,update_value):
    expense = session.query(Expense).filter_by(expense_id=expense_id).first()
    if expense:
        if update_type == "category":
            expense.expense_type = update_value
        elif update_type == "amount":
            expense.spent_amount = float(update_value)
        session.commit()
        print("Expense details updated.")
    else:
        print("Expense not found.")

def deleting_expense(expense_id):
    delexpense = session.query(Expense).filter(Expense.expense_id == expense_id).first()
    if delexpense:
        session.delete(delexpense)
        session.commit()
        print("Expense deleted.")
    else:
        print("Expense not found.")

def geocode_with_retry(geolocator, location):
        max_attempts = 4
        for attempt in range(max_attempts):
            try:
                return geolocator.geocode(location)
            except GeocoderTimedOut:
                if attempt < max_attempts - 1:
                    print("Service timed out. Retrying...")
                    time.sleep(4 ** attempt)  # Exponential backoff
                else:
                    raise


#start_place = "New York, NY"
#end_place = "Los Angeles, CA"
def calculating_distance(start_place, end_place):
    # Initialize the Nominatim geocoder (nominatim in locator finds coordinates of places)
    geolocator = Nominatim(user_agent = "calculate_distance")
    # get coordinates for start_place and destination_place
    #start = geolocator.geocode(start_place)
    #end = geolocator.geocode(end_place)
    start_coordinates = geocode_with_retry(geolocator, start_place)
    end_coordinates = geocode_with_retry(geolocator, end_place)
    #calculating distance in miles from coordinates (geodesic gives distance from coordinates)
    distance_miles = geodesic((start_coordinates.latitude,start_coordinates.longitude),(end_coordinates.latitude,end_coordinates.longitude)).miles
    # Assuming an average travel speed of 60 mph
    estimated_travel_time_hours = distance_miles / 60

    print(f"distance: {distance_miles:.2f}", f"time: {estimated_travel_time_hours:.2f}")
    
    return distance_miles
def calculate_trip_expense(trip):
    distance_miles = calculating_distance(trip.start_place,trip.end_place)
    gallons = distance_miles / (trip.fuel_efficiency_mpg or 1)
    trip_expense_cost = gallons * trip.avg_gas_price
    print(trip_expense_cost)
    return trip_expense_cost
def calculating_trip_cost(user_name):
    trips = session.query(Trip,User).join(User).filter(User.user_name == user_name).all()
    for trip in trips:
        if trip:
            start_place = trip.Trip.start_place
            end_place = trip.Trip.end_place
            distance_miles = calculating_distance(start_place, end_place)
            
            gallons = distance_miles / (trip.Trip.fuel_efficiency_mpg )
            trip_expense_cost = gallons * trip.Trip.avg_gas_price
            print(f"trip expense: {trip_expense_cost:.2f}")

def calculate_total_user_expense(user_id):
    user_trips = session.query(Trip).filter_by(user_id=user_id).all()
    totalExpense_Cost=0
    for trip in user_trips:
        print(trip)
        trip_expense_cost = calculate_trip_expense(trip)
        totalExpense_Cost = trip_expense_cost
        for expense in trip.expenses:
            print(expense)
            totalExpense_Cost +=expense.spent_amount
        print(f"totalExpense_Cost:{totalExpense_Cost}")
    return totalExpense_Cost

def calculate_total_expenses(user_name):
    user = session.query(User).filter_by(user_name=user_name).first()
    if user:
        user_id = user.user_id
        total_expense = calculate_total_user_expense(user_id)
        print(f"Total Expense for {user_name} : {total_expense}")   
