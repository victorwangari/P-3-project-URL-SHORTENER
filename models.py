from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password =  Column(String, nullable=False)
    urls = relationship('URL', back_populates='user')

class URL(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True, autoincrement=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='urls')