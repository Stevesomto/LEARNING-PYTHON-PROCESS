<<<<<<< HEAD
# WEB SCRAPPING IS THE PROCESS OF EXTRACTING DATA  AND INFORMATION FROM WEBSITES
# IT IS USED TO COLLECT DATA FROM WEB PAGES FOR ANALYSIS, RESEARCH, OR AUTOMATION PURPOSES
# WEB SCRAPPING CAN BE DONE USING VARIOUS TOOLS AND LIBRARIES SUCH AS BEAUTIFUL SOUP, SCRAPY, OR SELENIUM
# IT INVOLVES SENDING HTTP REQUESTS TO A WEB SERVER, RETRIEVING THE HTML CONTENT, AND PARSING IT TO EXTRACT THE DESIRED INFORMATION AND YOU MUST HAVE A KNOWLEDGE OF HTML AND CSS SELECTORS TO IDENTIFY THE ELEMENTS YOU WANT TO SCRAPE

# <html>
#     <head><title>Web Scraping Example</title></head>
#     <body>
#         <h1>Welcome to Web Scraping</h1>
#         <p>This is a simple example of a web page for scraping.</p>
#         <a href="https://example.com">Visit Example</a>
#     </body>
# </html>


import requests


url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)

if response.status_code == 200:
    print(response.text[:500])  # Print the first 500 characters of the page content
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    
    
    
# APPLYING BEAUTIFUL SOUP FOR PARSING HTML CONTENT
from bs4 import BeautifulSoup

html_content = "<html><head><title>Web Scraping Example</title></head><body><h1>Welcome to Web Scraping</h1><p>This is a simple example of a web page for scraping.</p><a href='https://example.com'>Visit Example</a></body></html>"

soup = BeautifulSoup(html_content, 'html.parser')
print(soup.h1.text)  # Output: Welcome to Web Scraping
print(soup.p.text)   # Output: This is a simple example of a web page for scraping.
print(soup.a['href'])  # Output: https://example.com


=======
# WEB SCRAPPING IS THE PROCESS OF EXTRACTING DATA  AND INFORMATION FROM WEBSITES
# IT IS USED TO COLLECT DATA FROM WEB PAGES FOR ANALYSIS, RESEARCH, OR AUTOMATION PURPOSES
# WEB SCRAPPING CAN BE DONE USING VARIOUS TOOLS AND LIBRARIES SUCH AS BEAUTIFUL SOUP, SCRAPY, OR SELENIUM
# IT INVOLVES SENDING HTTP REQUESTS TO A WEB SERVER, RETRIEVING THE HTML CONTENT, AND PARSING IT TO EXTRACT THE DESIRED INFORMATION AND YOU MUST HAVE A KNOWLEDGE OF HTML AND CSS SELECTORS TO IDENTIFY THE ELEMENTS YOU WANT TO SCRAPE

# <html>
#     <head><title>Web Scraping Example</title></head>
#     <body>
#         <h1>Welcome to Web Scraping</h1>
#         <p>This is a simple example of a web page for scraping.</p>
#         <a href="https://example.com">Visit Example</a>
#     </body>
# </html>


import requests


url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)

if response.status_code == 200:
    print(response.text[:500])  # Print the first 500 characters of the page content
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    
    
    
# APPLYING BEAUTIFUL SOUP FOR PARSING HTML CONTENT
from bs4 import BeautifulSoup

html_content = "<html><head><title>Web Scraping Example</title></head><body><h1>Welcome to Web Scraping</h1><p>This is a simple example of a web page for scraping.</p><a href='https://example.com'>Visit Example</a></body></html>"

soup = BeautifulSoup(html_content, 'html.parser')
print(soup.h1.text)  # Output: Welcome to Web Scraping
print(soup.p.text)   # Output: This is a simple example of a web page for scraping.
print(soup.a['href'])  # Output: https://example.com


>>>>>>> 5776d637b558ed6ad1589ad51c196b7c0d84fcfe
