#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Trip, Expense
import random
from datetime import datetime

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
        ('Finger Lakes, New York', 'Alexandria, Virginia',4.58,60,2),
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
