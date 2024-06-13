from Shortener import shorten_url, get_original_url, create_user

username = "vicky"
password = "1u28823"
create_user(username, password)

original_url = 'https://alison.com/?utm_source=google&utm_medium=cpc&utm_campaign=PPC_Tier-3_First-Click_Courses-_Broad_&utm_adgroup=Product_Academies&gclid=Cj0KCQiAutyfBhCMARIsAMgcRJSqIRBaFMrc1RNtdkG2j2duRvtp99QIof-EQilOZPynOpvUhySm93kaAjKQEALw_wcB&gclid=Cj0KCQiAutyfBhCMARIsAMgcRJSqIRBaFMrc1RNtdkG2j2duRvtp99QIof-EQilOZPynOpvUhySm93kaAjKQEALw_wcB'

short_url = shorten_url(original_url, username)
print(f"Original URL: {original_url} -> Short URL: {short_url}")
retrieved_url = get_original_url(short_url)
print(f"Short URL: {short_url} -> Retrieved URL: {retrieved_url}")
