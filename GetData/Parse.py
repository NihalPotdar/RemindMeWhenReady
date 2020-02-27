import requests
from bs4 import BeautifulSoup

# Social Media Page
URL = "https://nihalpotdar.github.io"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('')
# Printing out the content for testing
print(results.prettify())

