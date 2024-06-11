import string
from database import session
from models import URL , User

BASE62 = string.ascii_letters + string.digits
def encode_url(num):
    if num == 0:
        return BASE62[0]
    arr = []
    base = len(BASE62)
    while num:
        rem = num % base
        num //= base
        arr.append(BASE62[rem])
    arr.reverse()
    return ''.join(arr)

def decode_url(short_url):
    base = len(BASE62)
    strlen = len(short_url)
    num = 0

    for i, char in enumerate(short_url):
        power = strlen - (i + 1)
        num += BASE62.index(char) * (base ** power)
    return num

def shorten_url(original_url, username):
    user = session.query(User).filter_by(username=username).first()
    if not user:
        raise ValueError("User does not exist")
    
    new_url = URL(original_url, shortened_url='', user= user)
    session.add(new_url)
    session.commit()

    short_url = encode_url(new_url.id)
    new_url.shortened_url = short_url
    session.commit()

    return short_url

def get_original_url (short_url):
    url_id= decode_url(short_url)
    url_entry = session.query(URL).filter_by(id=url_id).first()
    return url_entry.original_url if url_entry else None

def create_user(username, password):
    if session.query(User).filter_by(username=username).first():
        raise ValueError("User already exists")
    new_user = User(username=username, password= password)
    session.add(new_user)
    session.commit()
    