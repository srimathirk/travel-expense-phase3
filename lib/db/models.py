from sqlalchemy import create_engine, MetaData, func, ForeignKey
from sqlalchemy import Column, Integer, String, Float, Table, DateTime
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

# to maintain consistency of database schema
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base=declarative_base(metadata=metadata)
#database connection 
engine = create_engine('sqlite:///travel_records.db')
Session = sessionmaker(bind=engine)
session = Session()

#User class (table)
class User(Base):
    __tablename__='users'
    user_id = Column(Integer(),primary_key=True)
    user_name = Column(String())
    mail_id = Column(String(),unique=True)
    phone_no = Column(String())
    created_at = Column(DateTime(),server_default=func.now())
    
    trips = relationship("Trip", back_populates='user')
    def __repr__(self):
        return f"User {self.user_id}: " \
            + f" Name {self.user_name}, " \
            + f" Email {self.mail_id}" \
            + f" Phone {self.phone_no}" \
            + f" at {self.created_at}"
   
#Trip class(table)
class Trip(Base):
    __tablename__ = 'trips'
    trip_id = Column(Integer(),primary_key=True)
    start_place = Column(String())
    end_place = Column(String())
    avg_gas_price = Column(Float())
    fuel_efficiency_mpg = Column(Integer())
    user_id = Column(Integer(),ForeignKey('users.user_id'))
    
    expenses = relationship('Expense', back_populates='trip')
    user = relationship('User', back_populates='trips')
    def __repr__(self):
        return f"Trip {self.trip_id}: " \
            + f" From {self.start_place}, " \
            + f" To {self.end_place}" \
            + f" Gas_price {self.avg_gas_price}$" \
            + f" MPG {self.fuel_efficiency_mpg}mpg"
    
#Expense class(table)
class Expense(Base):
    __tablename__='expenses'
    expense_id = Column(Integer(),primary_key=True)
    trip_id = Column(Integer(),ForeignKey('trips.trip_id'))
    expense_type = Column(String())
    spent_amount = Column(Float())
    
    trip = relationship('Trip',back_populates='expenses')
    def __repr__(self):
        return f" Expense {self.expense_id}: " \
            + f" Type {self.expense_type}, " \
            + f" Amount_spent {self.spent_amount}$"
