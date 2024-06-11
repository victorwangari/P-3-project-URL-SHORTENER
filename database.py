from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, URL

engine = create_engine('sqlite:///url_shortener.db')
Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
s = session()