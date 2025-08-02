<<<<<<< HEAD
# WIKIPEDIA ARTICLE SCRAPER
import requests
from bs4 import BeautifulSoup

# GET WIKIPEDIA ARTICLE URL FROM THE USER
def get_wikipedia_page(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code} Check th e topic name and try again.")
        return None

# EXTRACT TITLE 

def extract_title(soup):
   return soup.find('h1').text 

# EXTRACT SUMMARY
def extract_summary(soup):
    paragraphs = soup.find_all('p')
    for para in paragraphs:
        if para.text.strip():
            return para.text.strip()
    return "No summary found."

# EXTRACT THE HEADINGS
def get_headings(soup):
    headings = [heading.text.strip() for heading in soup.find_all(['h1', 'h3', 'h4'])] 
    return headings

# EXTRACT LINKS
def extracts_links(soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/wiki/') and ":" not in href:
            links.append(f"https://en.wikipedia.org{href}")
    return list(set(links))             # Remove duplicates

# MAIN FUNCTION TO SCRAPE WIKIPEDIA ARTICLE
def main(topic):
    topic = input(f"Enter the topic you want to scrape from Wikipedia: ").strip()
    page_content = get_wikipedia_page(topic)
    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        title = extract_title(soup)
        summary = extract_summary(soup)
        headings = get_headings(soup)
        links = extracts_links(soup)

        print("\n ----- Wikipedia article details-----")
        print(f"\nTitle: {title}")
        print(f"\nSummary: {summary}")
        print("\nHeadings:")
        for heading in headings:
            print(f"- {heading}")
        
        print("\nLinks:")
        for link in links:
            print(link)

# RUN THE MAIN FUNCTION
if __name__ == "__main__":
=======
# WIKIPEDIA ARTICLE SCRAPER
import requests
from bs4 import BeautifulSoup

# GET WIKIPEDIA ARTICLE URL FROM THE USER
def get_wikipedia_page(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code} Check th e topic name and try again.")
        return None

# EXTRACT TITLE 

def extract_title(soup):
   return soup.find('h1').text 

# EXTRACT SUMMARY
def extract_summary(soup):
    paragraphs = soup.find_all('p')
    for para in paragraphs:
        if para.text.strip():
            return para.text.strip()
    return "No summary found."

# EXTRACT THE HEADINGS
def get_headings(soup):
    headings = [heading.text.strip() for heading in soup.find_all(['h1', 'h3', 'h4'])] 
    return headings

# EXTRACT LINKS
def extracts_links(soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/wiki/') and ":" not in href:
            links.append(f"https://en.wikipedia.org{href}")
    return list(set(links))             # Remove duplicates

# MAIN FUNCTION TO SCRAPE WIKIPEDIA ARTICLE
def main(topic):
    topic = input(f"Enter the topic you want to scrape from Wikipedia: ").strip()
    page_content = get_wikipedia_page(topic)
    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        title = extract_title(soup)
        summary = extract_summary(soup)
        headings = get_headings(soup)
        links = extracts_links(soup)

        print("\n ----- Wikipedia article details-----")
        print(f"\nTitle: {title}")
        print(f"\nSummary: {summary}")
        print("\nHeadings:")
        for heading in headings:
            print(f"- {heading}")
        
        print("\nLinks:")
        for link in links:
            print(link)

# RUN THE MAIN FUNCTION
if __name__ == "__main__":
>>>>>>> 5776d637b558ed6ad1589ad51c196b7c0d84fcfe
    main("Python (programming language)") # Default topic, can be changed by user input