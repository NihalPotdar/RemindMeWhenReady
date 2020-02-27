import requests

# Social Media Page
page = requests.get("https://nihalpotdar.github.io")

# Printing out the content for testing
print(page.content)