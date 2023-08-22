from sqlalchemy import create_engine, MetaData, func, ForeignKey
from sqlalchemy import Column, Integer, String, Float, Table, DateTime
from sqlalchemy.orm import relationship, declarative_base

# to maintain consistency of database schema
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base=declarative_base(metadata=metadata)
#database connection 
engine = create_engine('sqlite:///travel_records.db')

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
            + f"Name {self.user_name}, " \
            + f"Email {self.mail_id}" \
            + f"Phone {self.phone_no}" \
            + f"at {self.created_at}"
