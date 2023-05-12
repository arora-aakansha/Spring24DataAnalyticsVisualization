import re
# Open the HTML file and read the content into a string
encodings = ['utf-8', 'iso-8859-1', 'cp1252']

for encoding in encodings:
    try:
        with open('wiki.html', 'r', encoding=encoding) as f:
            html_content = f.read()
        break
    except UnicodeDecodeError:
        continue
# print(html_content)

#change the tag of html
# Replace all <h1> tags with <h2> tags using regular expressions
html_content = re.sub(r'<h1\b', '<h2', html_content)
html_content = re.sub(r'</h1>', '</h2>', html_content)

# Replace all <div> tags with <article> tags using regular expressions
html_content = re.sub(r'<div\b', '<article', html_content)
html_content = re.sub(r'</div>', '</article>', html_content)

# Replace the string "old string" with "new string"
html_content = html_content.replace('that', 'this')
# print(html_content)

# Write the modified HTML content back to the file
with open('wiki.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
    

