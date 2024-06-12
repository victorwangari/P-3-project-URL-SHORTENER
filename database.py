from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Database setup
engine = create_engine('sqlite:///url_shortener.db')
Base.metadata.create_all(engine)

# Session factory
Session = sessionmaker(bind=engine)
