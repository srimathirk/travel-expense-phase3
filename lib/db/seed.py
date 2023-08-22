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
insert seed data
    names = ['Ganes', 'Mauli', 'Heshu', 'Indu', 'krish', 'Sundar', 'Rahman', 'Raja', 'GV', 'Ramya', 'Simma','Sachin']
    emails = ['gane@gmail.com','maUli@yahoo.com', 'Heshu@Yahoo.com', 'Gundu@Hotmail.com', 'Krish@Gmail.com', 'Sundae@gmail.com', 'rahman@raway.com','raja@ymail.com','gv@tamilan.com','ramy@ram.com','simma@gaho.com','sachin@gmail.com']
    phones = ['2318587894', '7414741474', '5588559898','8787878788', '9969658749', '8548785469','7878555544','8585777777', '7523232314', '4455787878','2255888888','7878999999']
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