#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User, Trip, Expense

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///travel_records.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()
