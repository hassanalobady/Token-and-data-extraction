import requests
from bs4 import BeautifulSoup

# Define the login URL and credentials of your portal
login_url = 'http://sgsportal.upm.edu.my:8080/sgsportal/' 
username = 'username'
password = 'password'

# Create a session to maintain the authentication cookies
session = requests.Session()

# Prepare the login data with the credentials
login_data = {
    'username': username,
    'password': password
}

# Send a POST request with the login data to authenticate
login_response = session.post(login_url, data=login_data)

# Check if the login was successful by analyzing the response
if login_response.status_code == 200:
    # If the login was successful, you can access authenticated pages using the session object
    data_page_response = session.get('http://sgsportal.upm.edu.my:8080/sgsportal/')
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(data_page_response.content, 'html.parser')
    
    # Find and extract the desired data (e.g., names and fields of study) from the page
    data_elements = soup.find_all('div', class_='data')
    
    for element in data_elements:
        Matric_No = element.find('span', class_='Matric_No').text
        Name = element.find('span', class_='Name').text
        
        # Print the extracted data
        print(f"Matric_No: {matric_No}")
        print(f"Name: {name}")
        print()
    
    # Close the session when finished
    session.close()
else:
    print("Login failed.")
