import requests

# Define the URL of the web page you want to fetch
url = "https://en.wikipedia.org/wiki/Main_Page"

# Send a GET request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Define the filename for the HTML file
filename = "wiki.html"

# Open the file for writing and write the HTML content
with open(filename, "wb") as f:
    f.write(html_content)

print("Web content saved to", filename)
