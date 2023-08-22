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
