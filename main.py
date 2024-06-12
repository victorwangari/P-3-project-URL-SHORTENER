from Shortener import shorten_url, get_original_url, create_user

username = "wanja"
password = "1u28823"
create_user(username, password)

original_url = 'https://replit.com/@victorwangari65/Nodejs#index.js'

short_url = shorten_url(original_url, username)
print(f"Original URL: {original_url} -> Short URL: {short_url}")
retrieved_url = get_original_url(short_url)
print(f"Short URL: {short_url} -> Retrieved URL: {retrieved_url}")
