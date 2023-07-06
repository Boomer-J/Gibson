import requests
from bs4 import BeautifulSoup
import re

# Specify the URL of the website to scrape
url = "https://example.com"

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object with the website's HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Define a regular expression pattern to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Find all organization names, emails, and phone numbers using appropriate HTML tags and attributes
organization_names = soup.find_all('h3', class_='org-name')
emails = re.findall(email_pattern, response.text)
phone_numbers = soup.find_all('span', class_='phone-number')

# Print the scraped data
for name in organization_names:
    print("Organization Name:", name.text.strip())

for email in emails:
    print("Email:", email)

for phone in phone_numbers:
    print("Phone Number:", phone.text.strip())
