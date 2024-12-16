# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  December 16, 2024 19:24:30
# Database: sqlite:////tmp/tmp.lck2pcukVO/GarageSystem_iter_1/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Garage(SAFRSBaseX, Base):
    """
    description: Represents a car garage.
    """
    __tablename__ = 'garage'
    _s_collection_name = 'Garage'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    capacity = Column(Integer)
    car_count = Column(Integer)
    employee_count = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    EmployeeList : Mapped[List["Employee"]] = relationship(back_populates="garage")



class Owner(SAFRSBaseX, Base):
    """
    description: Represents a car owner.
    """
    __tablename__ = 'owner'
    _s_collection_name = 'Owner'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    contact_number = Column(String)
    car_count = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    CarList : Mapped[List["Car"]] = relationship(back_populates="owner")



class Part(SAFRSBaseX, Base):
    """
    description: Represents a car part.
    """
    __tablename__ = 'part'
    _s_collection_name = 'Part'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    RepairList : Mapped[List["Repair"]] = relationship(back_populates="part")



class Vendor(SAFRSBaseX, Base):
    """
    description: Represents a vendor supplying car parts.
    """
    __tablename__ = 'vendor'
    _s_collection_name = 'Vendor'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_info = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)



class Car(SAFRSBaseX, Base):
    """
    description: Represents a car.
    """
    __tablename__ = 'car'
    _s_collection_name = 'Car'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    make = Column(String)
    year = Column(Integer)
    registration_number = Column(String)
    owner_id = Column(ForeignKey('owner.id'))
    service_count = Column(Integer)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("CarList"))

    # child relationships (access children)
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="car")
    ServiceList : Mapped[List["Service"]] = relationship(back_populates="car")



class Employee(SAFRSBaseX, Base):
    """
    description: Represents a garage employee.
    """
    __tablename__ = 'employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
    garage_id = Column(ForeignKey('garage.id'))

    # parent relationships (access parent)
    garage : Mapped["Garage"] = relationship(back_populates=("EmployeeList"))

    # child relationships (access children)



class Appointment(SAFRSBaseX, Base):
    """
    description: Represents an appointment for car service.
    """
    __tablename__ = 'appointment'
    _s_collection_name = 'Appointment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('car.id'))
    appointment_date = Column(Date)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("AppointmentList"))

    # child relationships (access children)



class Service(SAFRSBaseX, Base):
    """
    description: Represents a car service record.
    """
    __tablename__ = 'service'
    _s_collection_name = 'Service'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    car_id = Column(ForeignKey('car.id'))
    service_date = Column(Date)
    description = Column(String)
    repair_count = Column(Integer)

    # parent relationships (access parent)
    car : Mapped["Car"] = relationship(back_populates=("ServiceList"))

    # child relationships (access children)
    InvoiceList : Mapped[List["Invoice"]] = relationship(back_populates="service")
    RepairList : Mapped[List["Repair"]] = relationship(back_populates="service")



class Invoice(SAFRSBaseX, Base):
    """
    description: Represents an invoice for a car service.
    """
    __tablename__ = 'invoice'
    _s_collection_name = 'Invoice'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    service_id = Column(ForeignKey('service.id'))
    total_amount = Column(Integer)
    invoice_count = Column(Integer)

    # parent relationships (access parent)
    service : Mapped["Service"] = relationship(back_populates=("InvoiceList"))

    # child relationships (access children)



class Repair(SAFRSBaseX, Base):
    """
    description: Represents a car repair record.
    """
    __tablename__ = 'repair'
    _s_collection_name = 'Repair'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    service_id = Column(ForeignKey('service.id'))
    part_id = Column(ForeignKey('part.id'))
    repair_date = Column(Date)
    repair_cost_total = Column(Integer)

    # parent relationships (access parent)
    part : Mapped["Part"] = relationship(back_populates=("RepairList"))
    service : Mapped["Service"] = relationship(back_populates=("RepairList"))

    # child relationships (access children)
