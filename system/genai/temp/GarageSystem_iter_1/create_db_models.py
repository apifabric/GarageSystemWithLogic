# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Garage(Base):
    """description: Represents a car garage."""
    __tablename__ = 'garage'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)  # Garage name
    location = Column(String)  # Location of the garage
    capacity = Column(Integer)  # Number of cars the garage can hold
    car_count = Column(Integer, default=0)  # Derived car count
    employee_count = Column(Integer, default=0)  # Derived employee count


class Car(Base):
    """description: Represents a car."""
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String)  # Car model
    make = Column(String)  # Car make
    year = Column(Integer)  # Manufacturing year
    registration_number = Column(String)  # Registration number
    owner_id = Column(Integer, ForeignKey('owner.id'))  # ID of the owner
    service_count = Column(Integer, default=0)  # Derived service count


class Owner(Base):
    """description: Represents a car owner."""
    __tablename__ = 'owner'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)  # Owner name
    address = Column(String)  # Owner address
    contact_number = Column(String)  # Contact number
    car_count = Column(Integer, default=0)  # Derived car count


class Service(Base):
    """description: Represents a car service record."""
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('car.id'))  # ID of the car
    service_date = Column(Date)  # Date of service
    description = Column(String)  # Description of the service
    repair_count = Column(Integer, default=0)  # Derived repair count


class Employee(Base):
    """description: Represents a garage employee."""
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)  # Employee name
    role = Column(String)  # Employee role
    garage_id = Column(Integer, ForeignKey('garage.id'))  # ID of the garage they work for


class Part(Base):
    """description: Represents a car part."""
    __tablename__ = 'part'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)  # Part name
    price = Column(Integer)  # Part price


class Repair(Base):
    """description: Represents a car repair record."""
    __tablename__ = 'repair'

    id = Column(Integer, primary_key=True, autoincrement=True)
    service_id = Column(Integer, ForeignKey('service.id'))  # Associated service
    part_id = Column(Integer, ForeignKey('part.id'))  # Part used
    repair_date = Column(Date)  # Date of repair
    repair_cost_total = Column(Integer, default=0)  # Sum of repair costs


class Appointment(Base):
    """description: Represents an appointment for car service."""
    __tablename__ = 'appointment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('car.id'))  # Car ID for appointment
    appointment_date = Column(Date)  # Appointment date


class Invoice(Base):
    """description: Represents an invoice for a car service."""
    __tablename__ = 'invoice'

    id = Column(Integer, primary_key=True, autoincrement=True)
    service_id = Column(Integer, ForeignKey('service.id'))  # Service ID
    total_amount = Column(Integer)  # Total amount charged
    invoice_count = Column(Integer, default=0)  # Derived invoice count


class Vendor(Base):
    """description: Represents a vendor supplying car parts."""
    __tablename__ = 'vendor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)  # Vendor name
    contact_info = Column(String)  # Vendor contact information


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    garage1 = Garage(name="City Center Garage", location="Downtown", capacity=100, car_count=0, employee_count=0)
    garage2 = Garage(name="Suburban Auto", location="Suburb", capacity=50, car_count=0, employee_count=0)
    garage3 = Garage(name="Rural Roadside", location="Countryside", capacity=30, car_count=0, employee_count=0)
    garage4 = Garage(name="Highway Hub", location="Highway", capacity=200, car_count=0, employee_count=0)
    car1 = Car(model="Model S", make="Tesla", year=2020, registration_number="123ABC", owner_id=1, service_count=0)
    car2 = Car(model="Accord", make="Honda", year=2018, registration_number="456DEF", owner_id=2, service_count=0)
    car3 = Car(model="F-150", make="Ford", year=2021, registration_number="789GHI", owner_id=1, service_count=0)
    car4 = Car(model="Corolla", make="Toyota", year=2019, registration_number="012JKL", owner_id=3, service_count=0)
    owner1 = Owner(name="Alice Johnson", address="123 Elm St", contact_number="555-0123", car_count=0)
    owner2 = Owner(name="Bob Smith", address="456 Maple Dr", contact_number="555-4567", car_count=0)
    owner3 = Owner(name="Carol King", address="789 Oak Ave", contact_number="555-7890", car_count=0)
    owner4 = Owner(name="Dave Lee", address="321 Pine Rd", contact_number="555-3210", car_count=0)
    service1 = Service(car_id=1, service_date=date(2023, 7, 25), description="Oil change", repair_count=0)
    service2 = Service(car_id=2, service_date=date(2023, 6, 14), description="Tire rotation", repair_count=0)
    service3 = Service(car_id=3, service_date=date(2023, 8, 10), description="Brake inspection", repair_count=0)
    service4 = Service(car_id=4, service_date=date(2023, 5, 5), description="Battery replacement", repair_count=0)
    employee1 = Employee(name="Eve Turner", role="Mechanic", garage_id=1)
    employee2 = Employee(name="Frank White", role="Receptionist", garage_id=2)
    employee3 = Employee(name="Grace Hill", role="Manager", garage_id=1)
    employee4 = Employee(name="Hank Green", role="Technician", garage_id=3)
    part1 = Part(name="Brake Pad", price=80)
    part2 = Part(name="Oil Filter", price=20)
    part3 = Part(name="Spark Plug", price=10)
    part4 = Part(name="Car Battery", price=120)
    repair1 = Repair(service_id=1, part_id=2, repair_date=date(2023, 7, 26), repair_cost_total=0)
    repair2 = Repair(service_id=2, part_id=1, repair_date=date(2023, 6, 15), repair_cost_total=0)
    repair3 = Repair(service_id=3, part_id=3, repair_date=date(2023, 8, 11), repair_cost_total=0)
    repair4 = Repair(service_id=4, part_id=4, repair_date=date(2023, 5, 6), repair_cost_total=0)
    appointment1 = Appointment(car_id=1, appointment_date=date(2023, 8, 15))
    appointment2 = Appointment(car_id=2, appointment_date=date(2023, 8, 25))
    appointment3 = Appointment(car_id=3, appointment_date=date(2023, 9, 5))
    appointment4 = Appointment(car_id=4, appointment_date=date(2023, 9, 15))
    invoice1 = Invoice(service_id=1, total_amount=150, invoice_count=0)
    invoice2 = Invoice(service_id=2, total_amount=200, invoice_count=0)
    invoice3 = Invoice(service_id=3, total_amount=180, invoice_count=0)
    invoice4 = Invoice(service_id=4, total_amount=250, invoice_count=0)
    vendor1 = Vendor(name="Auto Parts Co.", contact_info="autoparts@example.com")
    vendor2 = Vendor(name="Car Essentials Inc.", contact_info="careessentials@example.com")
    vendor3 = Vendor(name="Vehicle Supplies Ltd.", contact_info="vehiclesupplies@example.com")
    vendor4 = Vendor(name="Motor Elements LLC.", contact_info="motorelements@example.com")
    
    
    
    session.add_all([garage1, garage2, garage3, garage4, car1, car2, car3, car4, owner1, owner2, owner3, owner4, service1, service2, service3, service4, employee1, employee2, employee3, employee4, part1, part2, part3, part4, repair1, repair2, repair3, repair4, appointment1, appointment2, appointment3, appointment4, invoice1, invoice2, invoice3, invoice4, vendor1, vendor2, vendor3, vendor4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
