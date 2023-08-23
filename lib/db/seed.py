#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Trip, Expense
import random
from datetime import datetime
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut
import time



if __name__ == '__main__':
    #databasse connection
    engine = create_engine('sqlite:///travel_records.db')
    #Base.metadata.create_all(engine)

    #create a session 
    Session = sessionmaker(bind=engine)
    session = Session()

#deleting old populated seed to make sure everything works fine
    session.query(User).delete()
    session.query(Trip).delete()
    session.query(Expense).delete()
    print("starting seed populates")
    session.commit()
#insert user data
    names = ['Ganes', 'Mauli', 'Heshu', 'Indu', 'krish', 'Sundar', 'Rahman', 'Raja', 'GV', 'Ramya', 'Simma','Sachin']
    emails = ['gane@gmail.com','maUli@yahoo.com', 'Heshu@Yahoo.com', 'Gundu@Hotmail.com', 'Krish@Gmail.com', 'Sundae@gmail.com', 'rahman@raway.com','raja@ymail.com','gv@tamilan.com','ramy@ram.com','simma@gaho.com','sachin@gmail.com']
    phones = ['2318587894', '7414741474', '5588559898','8787878788', '9969658749', '8548785469','7878555544','8585777777', '7523232314', '4455787878','2255888888','7878999999']
    #seed data
    users = []
    for name,phone,email in zip(names,emails,phones):
        #zip iterates through names,phones,emails lists simultaneously
        user =  User(
            user_name = name,
            mail_id = email,
            phone_no = phone,
            created_at = datetime.now()
        )
        # add and commit individually to get IDs back
        session.add(user)
        users.append(user)
    session.commit()

    #insert tripdata
    trip_datas = [
        ('Princeton, New Jersey','Philadelphia',3.82,50,5),
        ('Catskills, New York','Lexington, Massachusetts',4.75,45,4),
        ('New York City, NY', 'Los Angeles, CA',4.58,60,2),
        ('Westerly, Rhode Island','Cape May, New Jersey',3.64,50,1),
        ('Devils Tower, Wyoming','Niagara Falls',4.11,45,3),
        ('Philadelphia','Southampton Beach, Long Island',4.11,55,5),
        ('Montreal, Canada', 'New Jersey',3.64,55,4),
        ('Chincoteague Island, Virginia', 'Franconia, New Hampshire',3.72,55,6),
        ('The Skyline Drive, Virginia','Jersey City, NJ',3.64,55,7),
        ('Moab, Utah', 'Camden, Maine',3.77,55,8),
        ('Austin, Texas','Zion National Park',3.60,55,9),
        ('Seneca Falls, New York','Princeton, New Jersey',4.05,65,12),
        ('Southampton Beach, Long Island','Kent, Connecticut',5.5,65,11),
        ('Killington, Vermont','Big Sur, California',3.81,65,10),
        ('Hershey, Pennsylvania','Washington DC',3.99,65,8),
        ('Atlantic City, New Jersey','Hudson Valley, New York',4.54,65,9),
        ('Brandywine Valley, Pennsylvania', 'Atlantic City, New Jersey',3.25,45,6),
        ('Kent, Connecticut','The Poconos Mountains',3.17,50,4)
    ]
    #seed data
    trips=[]
    for start_place,end_place,avg_gas_price,fuel_efficiency_mpg,user_id in trip_datas:
        trip = Trip(
            start_place=start_place,
            end_place=end_place,
            avg_gas_price=avg_gas_price,
            fuel_efficiency_mpg=fuel_efficiency_mpg,
            user_id=user_id
        )
        session.add(trip)
        trips.append(trip)
    #commiting change
    session.commit()
    #geolocator = Nominatim(user_agent="my_app")
    def geocode_with_retry(geolocator, location):
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                return geolocator.geocode(location)
            except GeocoderTimedOut:
                if attempt < max_attempts - 1:
                    print("Service timed out. Retrying...")
                    time.sleep(2 ** attempt)  # Exponential backoff
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

    #insert expense data
    expense_data = [
        (1,'Food',55),(1,'Accomodation',240),(1,'Parking',50),
        (2,'Food',60),(2,'Parking',50),(2,'Entrance',70),
        (3,'Beverages',32),(3,'Accomodation',150),
        (4,'MuseumTickets', 50),(4,'Souvenirs',60),(4,'Parking',60),
        (5,'Food',60),(5,'Accomodation',155),
        (6,'Parking',20),(6,'Souvenirs',60),(6,'Food',30),
        (7,'ThemePark',100),
        (8,'Parking',20),(8,'Food',40),
        (9,'MuseumTickets',50),(9,'Accomodation',100),
        (10,'Parking',20),(10,'ThemePark',75),(10,'Food',60),
        (11,'Food',50),
        (12,'ThemePark',70),(12,'Accomodation',120),(12,'Food',30),
        (13,'Accomodation',120),(13,'Souvenirs',150),
        (14,'MuseumTickets',60),(14,'Parking',50),(14,'Food',20),
        (15,'Food',60),(15,'Accomodation',120),
        (16,'Accomodation',150),(16,'Food',100),(16,'Parking',50),
        (17,'Parking',20),(17,'Food',150),
        (18,'Accomodation',160)
    ]    
    #seed data
    expenses=[]
    for trip_id,expense_type,spent_amount in expense_data:
        expense = Expense(
            trip_id=trip_id,
            expense_type=expense_type,
            spent_amount=spent_amount
        )
        session.add(expense)
        expenses.append(expense)
    session.commit()   
    
    
    
    # geolocator = Nominatim(user_agent="my_app")
    # def geocode_retry(location):
    #     max_attempts = 3
    #     for attempt in range(max_attempts):
    #         try:
    #             return geolocator.geocode(location)
    #         except GeocoderTimedOut:
    #             if attempt < max_attempts -1:
    #                 print ("service time out, retry")
    #                 time.sleep(2 ** attempt)
    #             else:
    #                 raise
    # # Provide the location
    # location = "New York, NY"
    # # Get the coordinates (latitude and longitude) for the location with retries
    # coords = geocode_retry(location)
    # # Print the coordinates
    # print(f"Coordinates for {location}: Latitude {coords.latitude}, Longitude {coords.longitude}")

    #import ipdb; ipdb.set_trace()
    session.close()
    #test
    # user1 = session.query(User).first()
    # print(user1)
    # users = session.query(User).all()
    # print(users)
    # user5 = session.query(User).filter_by(user_name = 'Heshu').all()
    # print(user5)
    # user6 = session.query(User).filter(User.user_name.ilike('%i%')).all()
    # print(user6)
    # i='sun'
    # userf = session.query(User).filter(User.user_name.like('%{}%'.format(i))).all()
    # print(userf)
    # user8 = session.query(User).filter(User.user_id >5).all()
    # print(user8)
    # testing trips
    #getting trip details with userid
    # user_trips = session.query(Trip).filter_by(user_id=6).all()
    # print(user_trips) 
    #getting trip details by username
    # user_trips = session.query(Trip).join(User).filter(User.user_name=='Sundar').all()
    # print(user_trips)
    #filtering trip and user based on mileage
    # user_trip1 = session.query(Trip,User).join(User).filter(Trip.fuel_efficiency_mpg < 50).all()
    # print(user_trip1)
    # trip = session.query(Trip).filter_by(trip_id = 3).first()
    # if trip:
    #     start_place = trip.start_place
    #     end_place = trip.end_place
    #     distance = calculating_distance(start_place,end_place)
    #     print(f"Distance: {distance:.2f}miles ")
    
    # calculating total expense by using username associated with trip
    # trip = session.query(Trip,User).join(User).filter(User.user_name == 'Heshu').first()
    # if trip:
    #     start_place = trip.Trip.start_place
    #     end_place = trip.Trip.end_place
    #     distance_miles = calculating_distance(start_place, end_place)
        
    #     gallons = distance_miles / (trip.Trip.fuel_efficiency_mpg )
    #     trip_expense_cost = gallons * trip.Trip.avg_gas_price
    #     print(f"trip expense: {trip_expense_cost:.2f}")

    ##getting warning because not using jointable , above was the correccted code
    # trip,user = session.query(Trip,User).filter(User.user_name == 'Heshu').first()
    # if trip and user:
    #     start_place = trip.start_place
    #     end_place = trip.end_place
    #     distance_miles = calculating_distance(start_place, end_place)
        
    #     gallons = distance_miles / (trip.fuel_efficiency_mpg or 1)
    #     trip_expense_cost = gallons * trip.avg_gas_price
    #     print(trip_expense_cost)

    #testing expense dbtable

    ##printing trips and associated expense details based on user_id 
    # user_trips = session.query(Trip).filter_by(user_id=4).all()
    # for trip in user_trips:
    #     print(trip)
    #     # Access associated expenses and print their details
    #     for expense in trip.expenses:
    #         print( expense)
        ##printing trips and associated expense details with total cost    
    # user_trips = session.query(Trip).filter_by(user_id=3).all()
    # totalExpense_Cost=0
    # for trip in user_trips:
    #     print(trip)
    #     for expense in trip.expenses:
    #         print(expense)
    #         totalExpense_Cost +=expense.spent_amount
    #     print(f"totalExpense_Cost:{totalExpense_Cost}")


    def calculate_trip_expense(trip):
        distance_miles = calculating_distance(trip.start_place,trip.end_place)
        gallons = distance_miles / (trip.fuel_efficiency_mpg or 1)
        trip_expense_cost = gallons * trip.avg_gas_price
        print(trip_expense_cost)
        return trip_expense_cost
    # user_trips = session.query(Trip).filter_by(user_id=9).all()
    # #totalExpense_Cost=0
    # for trip in user_trips:
    #     print(trip)
    #     trip_expense_cost = calculate_trip_expense(trip)
    #     totalExpense_Cost = trip_expense_cost
    #     for expense in trip.expenses:
    #         print(expense)
    #         totalExpense_Cost +=expense.spent_amount
    #     print(f"totalExpense_Cost:{totalExpense_Cost}")

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


    # #calculating total_expense using user_name
    # user_name = 'GV'
    # user = session.query(User).filter_by(user_name=user_name).first()
    # if user:
    #     user_id = user.user_id
    #     total_expense = calculate_total_user_expense(user_id)
    #     print(f"Total Expense for {user_name} : {total_expense}")   