import string
import requests
from database import Session
from models import URL, User

BASE62 = string.ascii_letters + string.digits
DOMAIN = 'https://short.ly/'

def encode_url(num, min_length=6):
    if num == 0:
        return BASE62[0]
    arr = []
    base = len(BASE62)
    while num:
        rem = num % base
        num //= base
        arr.append(BASE62[rem])
    arr.reverse()
    padded_url = ''.join(arr).zfill(min_length)
    return f'{DOMAIN}{padded_url}'

def decode_url(short_url):
    short_code = short_url.replace(DOMAIN, '')  # Remove domain part
    base = len(BASE62)
    strlen = len(short_code)
    num = 0

    for i, char in enumerate(short_code):
        power = (strlen - (i + 1))
        num += BASE62.index(char) * (base ** power)
    return num

def shorten_url(original_url, username):
    session = Session()  
    try:
        user = session.query(User).filter_by(username=username).first()
        if not user:
            raise ValueError("User does not exist")
        
        new_url = URL(original_url=original_url, short_url='', user=user)
        session.add(new_url)
        session.commit()

        short_url = encode_url(new_url.id)  # Use encode_url with min_length
        new_url.short_url = short_url
        session.commit()

        return short_url
    finally:
        session.close()  # Ensure the session is closed

def get_original_url(short_url):
    session = Session()  # Create a new session instance
    try:
        url_id = decode_url(short_url)
        url_entry = session.query(URL).filter_by(id=url_id).first()
        return url_entry.original_url if url_entry else None
    finally:
        session.close()  # Ensure the session is closed

# def create_user(username, password): 
#     session = Session()  # Create a new session instance
#     try:
#         if session.query(User).filter_by(username=username).first():
#             raise ValueError("User already exists")
#         new_user = User(username=username, password=password)
#         session.add(new_user)
#         session.commit()
#         return new_user
#     finally:
    
#         session.close()  # Ensure the session is closed
