import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to access
url = "https://en.wikipedia.org/wiki/Main_Page"

# Send a GET request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find and print the title of the page
title = soup.title.string
print("Title:", title)

# Find and print all the links on the page
links = soup.find_all("a")
for link in links:
    href = link.get("href")
    if href is not None:
        print("Link:", href)
