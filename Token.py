import requests
from bs4 import BeautifulSoup

# Create a session object
session = requests.Session()

# Login credentials
login_data = {
    'username': 'username',
    'password': 'password'
}

# Send a POST request to the login URL
login_url = 'http://119.40.116.236:8080/'  # Replace with the actual login URL
response = session.post(login_url, data=login_data)

# Check if login was successful (optional)
if response.status_code == 200:
    print("Login successful!")
else:
    print("Login failed.")

# Scrape a page that requires login
scrape_url = 'http://sgsportal.upm.edu.my:8080/sgsportal/'  # Replace with the actual page URL
response = session.get(scrape_url)

# Extract the cookies
cookies = session.cookies.get_dict()
print("Cookies:", cookies)
