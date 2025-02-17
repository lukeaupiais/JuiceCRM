from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    amount = Column(Float)
    status = Column(String)

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    description = Column(String)
    status = Column(String)
    priority = Column(String)