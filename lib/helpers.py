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

