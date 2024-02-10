import requests
from bs4 import BeautifulSoup
import json

# Function to scrape data from the website
def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find relevant elements and extract data
        data = []
        for item in soup.find_all('div', class_='item'):
            title = item.find('h2').text.strip()
            description = item.find('p').text.strip()
            
            # Append data to the list
            data.append({
                'title': title,
                'description': description
            })
        
        return data
    else:
        print('Failed to retrieve data from the website.')
        return None

# URL of the website to scrape
url = 'https://example.com'

# Scrape data from the website
scraped_data = scrape_website(url)

# Save the scraped data to a JSON file
if scraped_data:
    with open('scraped_data.json', 'w') as f:
        json.dump(scraped_data, f, indent=4)
    print('Scraped data saved to "scraped_data.json"')
