import requests

# Define the URL of the Wikipedia main page
url = "https://en.wikipedia.org/wiki/Main_Page"

# Send a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # If the request was successful, get the text content of the page
    text_content = response.text
    
    # Save the text content to a file using UTF-8 encoding
    with open("wikipedia_main_page.txt", "w", encoding="utf-8") as file:
        file.write(text_content)
        
    print("Data saved to file successfully.")
else:
    # If the request was unsuccessful, print the status code
    print("Error: " + str(response.status_code))
